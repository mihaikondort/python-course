import asyncio
import threading

import pytest

from interview_prep.pythonic.concurrency import (
    ThreadSafeCounter,
    gather_with_limit,
    parallel_map,
    producer_consumer,
    with_timeout,
)


def double(n: int) -> int:
    return n * 2


class TestParallelMap:
    def test_preserves_order(self):
        assert parallel_map(double, [1, 2, 3, 4]) == [2, 4, 6, 8]

    def test_empty(self):
        assert parallel_map(double, []) == []

    def test_propagates_exceptions(self):
        def boom(n):
            raise ValueError(n)

        with pytest.raises(ValueError):
            parallel_map(boom, [1])

    def test_actually_concurrent(self):
        import time

        def slow(_):
            time.sleep(0.1)
            return 1

        start = time.monotonic()
        parallel_map(slow, list(range(8)), workers=8)
        assert time.monotonic() - start < 0.5


class TestThreadSafeCounter:
    def test_increment_decrement(self):
        c = ThreadSafeCounter()
        c.increment()
        c.increment(5)
        c.decrement(2)
        assert c.value == 4

    def test_start_value(self):
        assert ThreadSafeCounter(10).value == 10

    def test_no_lost_updates(self):
        counter = ThreadSafeCounter()

        def work():
            for _ in range(10_000):
                counter.increment()

        threads = [threading.Thread(target=work) for _ in range(4)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        assert counter.value == 40_000


class TestGatherWithLimit:
    def test_preserves_order(self):
        async def value(n):
            await asyncio.sleep(0.01 * (5 - n))
            return n

        result = asyncio.run(gather_with_limit([value(i) for i in range(5)], limit=2))
        assert result == [0, 1, 2, 3, 4]

    def test_respects_limit(self):
        active = 0
        peak = 0

        async def track():
            nonlocal active, peak
            active += 1
            peak = max(peak, active)
            await asyncio.sleep(0.01)
            active -= 1

        asyncio.run(gather_with_limit([track() for _ in range(10)], limit=3))
        assert peak <= 3

    def test_empty(self):
        assert asyncio.run(gather_with_limit([], limit=2)) == []


class TestWithTimeout:
    def test_returns_result_when_fast(self):
        async def fast():
            return "done"

        assert asyncio.run(with_timeout(fast(), 1.0, "default")) == "done"

    def test_returns_default_on_timeout(self):
        async def slow():
            await asyncio.sleep(5)
            return "never"

        assert asyncio.run(with_timeout(slow(), 0.05, "default")) == "default"


class TestProducerConsumer:
    def test_processes_all_items(self):
        items = list(range(20))
        result = asyncio.run(producer_consumer(items, consumers=4))
        assert sorted(result) == items

    def test_empty(self):
        assert asyncio.run(producer_consumer([], consumers=2)) == []
