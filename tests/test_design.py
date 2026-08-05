import pytest

from interview_prep.design.event_bus import EventBus, StateMachine
from interview_prep.design.lru_cache import LRUCache, TTLCache
from interview_prep.design.rate_limiter import SlidingWindowLimiter, TokenBucket


class FakeClock:
    """A manually advanced clock for testing time-dependent code."""

    def __init__(self, start: float = 0.0) -> None:
        self.now = start

    def __call__(self) -> float:
        return self.now

    def advance(self, seconds: float) -> None:
        self.now += seconds


class TestLRUCache:
    def test_get_and_put(self):
        cache = LRUCache(2)
        cache.put("a", 1)
        assert cache.get("a") == 1

    def test_missing_returns_none(self):
        assert LRUCache(2).get("missing") is None

    def test_evicts_least_recently_used(self):
        cache = LRUCache(2)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.put("c", 3)
        assert cache.get("a") is None
        assert cache.get("b") == 2

    def test_get_refreshes_recency(self):
        cache = LRUCache(2)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.get("a")
        cache.put("c", 3)
        assert cache.get("a") == 1
        assert cache.get("b") is None

    def test_update_refreshes_recency(self):
        cache = LRUCache(2)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.put("a", 10)
        cache.put("c", 3)
        assert cache.get("a") == 10
        assert cache.get("b") is None

    def test_len_and_contains(self):
        cache = LRUCache(2)
        cache.put("a", 1)
        assert len(cache) == 1
        assert "a" in cache
        assert "b" not in cache

    def test_contains_has_no_side_effect(self):
        cache = LRUCache(2)
        cache.put("a", 1)
        cache.put("b", 2)
        assert "a" in cache  # must NOT count as a use
        cache.put("c", 3)
        assert "a" not in cache

    def test_invalid_capacity(self):
        with pytest.raises(ValueError):
            LRUCache(0)


class TestTTLCache:
    def test_returns_before_expiry(self):
        clock = FakeClock()
        cache = TTLCache(ttl=10, time_func=clock)
        cache.put("a", 1)
        clock.advance(9)
        assert cache.get("a") == 1

    def test_expires(self):
        clock = FakeClock()
        cache = TTLCache(ttl=10, time_func=clock)
        cache.put("a", 1)
        clock.advance(11)
        assert cache.get("a") is None

    def test_put_refreshes_expiry(self):
        clock = FakeClock()
        cache = TTLCache(ttl=10, time_func=clock)
        cache.put("a", 1)
        clock.advance(9)
        cache.put("a", 2)
        clock.advance(9)
        assert cache.get("a") == 2


class TestTokenBucket:
    def test_allows_up_to_capacity(self):
        bucket = TokenBucket(capacity=3, refill_rate=1, time_func=FakeClock())
        assert [bucket.allow() for _ in range(4)] == [True, True, True, False]

    def test_refills_over_time(self):
        clock = FakeClock()
        bucket = TokenBucket(capacity=2, refill_rate=1, time_func=clock)
        bucket.allow()
        bucket.allow()
        assert bucket.allow() is False
        clock.advance(1)
        assert bucket.allow() is True

    def test_does_not_exceed_capacity(self):
        clock = FakeClock()
        bucket = TokenBucket(capacity=2, refill_rate=1, time_func=clock)
        clock.advance(100)
        assert bucket.available == 2

    def test_multi_token_request(self):
        bucket = TokenBucket(capacity=5, refill_rate=1, time_func=FakeClock())
        assert bucket.allow(3) is True
        assert bucket.allow(3) is False
        assert bucket.allow(2) is True


class TestSlidingWindowLimiter:
    def test_limits_within_window(self):
        limiter = SlidingWindowLimiter(limit=2, window=10, time_func=FakeClock())
        assert [limiter.allow("user") for _ in range(3)] == [True, True, False]

    def test_keys_are_independent(self):
        limiter = SlidingWindowLimiter(limit=1, window=10, time_func=FakeClock())
        assert limiter.allow("a") is True
        assert limiter.allow("b") is True
        assert limiter.allow("a") is False

    def test_window_slides(self):
        clock = FakeClock()
        limiter = SlidingWindowLimiter(limit=1, window=10, time_func=clock)
        assert limiter.allow("a") is True
        clock.advance(11)
        assert limiter.allow("a") is True

    def test_remaining(self):
        limiter = SlidingWindowLimiter(limit=3, window=10, time_func=FakeClock())
        assert limiter.remaining("a") == 3
        limiter.allow("a")
        assert limiter.remaining("a") == 2


class TestEventBus:
    def test_publish_calls_handlers(self):
        received = []
        bus = EventBus()
        bus.subscribe("tick", received.append)
        assert bus.publish("tick", 1) == 1
        assert received == [1]

    def test_multiple_handlers_in_order(self):
        order = []
        bus = EventBus()
        bus.subscribe("e", lambda: order.append("first"))
        bus.subscribe("e", lambda: order.append("second"))
        bus.publish("e")
        assert order == ["first", "second"]

    def test_publish_to_unknown_event(self):
        assert EventBus().publish("nothing") == 0

    def test_unsubscribe_via_returned_callable(self):
        received = []
        bus = EventBus()
        off = bus.subscribe("e", received.append)
        off()
        bus.publish("e", 1)
        assert received == []

    def test_unsubscribe_unknown_handler_is_noop(self):
        EventBus().unsubscribe("e", print)

    def test_failing_handler_does_not_block_others(self):
        received = []

        def boom():
            raise ValueError("boom")

        bus = EventBus()
        bus.subscribe("e", boom)
        bus.subscribe("e", lambda: received.append("ran"))
        with pytest.raises(ExceptionGroup):
            bus.publish("e")
        assert received == ["ran"]

    def test_subscribers_returns_a_copy(self):
        bus = EventBus()
        bus.subscribe("e", print)
        bus.subscribers("e").clear()
        assert len(bus.subscribers("e")) == 1


class TestStateMachine:
    @pytest.fixture
    def machine(self):
        return StateMachine(
            initial="idle",
            transitions={
                ("idle", "start"): "running",
                ("running", "pause"): "paused",
                ("paused", "start"): "running",
                ("running", "stop"): "idle",
            },
        )

    def test_initial_state(self, machine):
        assert machine.state == "idle"

    def test_valid_transition(self, machine):
        assert machine.fire("start") == "running"
        assert machine.state == "running"

    def test_invalid_transition_raises_and_keeps_state(self, machine):
        with pytest.raises(ValueError):
            machine.fire("pause")
        assert machine.state == "idle"

    def test_can_fire(self, machine):
        assert machine.can_fire("start") is True
        assert machine.can_fire("pause") is False

    def test_history(self, machine):
        machine.fire("start")
        machine.fire("pause")
        assert machine.history == [("idle", "start", "running"), ("running", "pause", "paused")]
