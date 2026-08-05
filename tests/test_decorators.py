import pytest

from interview_prep.pythonic.decorators import (
    count_calls,
    memoize,
    retry,
    singleton,
    timer,
    validate_types,
)


class TestTimer:
    def test_returns_result(self):
        @timer
        def add(a, b):
            return a + b

        assert add(2, 3) == 5

    def test_records_duration(self):
        @timer
        def noop():
            return None

        noop()
        noop()
        assert len(noop.__wrapped_durations__) == 2
        assert all(d >= 0 for d in noop.__wrapped_durations__)

    def test_preserves_metadata(self):
        @timer
        def documented():
            """A docstring."""

        assert documented.__name__ == "documented"
        assert documented.__doc__ == "A docstring."


class TestMemoize:
    def test_caches(self):
        calls = []

        @memoize
        def square(n):
            calls.append(n)
            return n * n

        assert square(4) == 16
        assert square(4) == 16
        assert calls == [4]

    def test_handles_kwargs(self):
        calls = []

        @memoize
        def combine(a, b=1):
            calls.append((a, b))
            return a + b

        assert combine(1, b=2) == 3
        assert combine(1, b=2) == 3
        assert combine(1, b=3) == 4
        assert len(calls) == 2

    def test_cache_info_and_clear(self):
        @memoize
        def identity(n):
            return n

        identity(1)
        identity(1)
        identity(2)
        hits, misses = identity.cache_info()
        assert (hits, misses) == (1, 2)

        identity.cache_clear()
        assert identity.cache_info() == (0, 0)


class TestRetry:
    def test_succeeds_after_failures(self):
        attempts = []

        @retry(times=3)
        def flaky():
            attempts.append(1)
            if len(attempts) < 3:
                raise ValueError("not yet")
            return "ok"

        assert flaky() == "ok"
        assert len(attempts) == 3

    def test_reraises_after_exhaustion(self):
        attempts = []

        @retry(times=2)
        def always_fails():
            attempts.append(1)
            raise ValueError("nope")

        with pytest.raises(ValueError, match="nope"):
            always_fails()
        assert len(attempts) == 2

    def test_only_retries_listed_exceptions(self):
        attempts = []

        @retry(times=3, exceptions=(ValueError,))
        def wrong_error():
            attempts.append(1)
            raise TypeError("different")

        with pytest.raises(TypeError):
            wrong_error()
        assert len(attempts) == 1

    def test_invalid_times(self):
        with pytest.raises(ValueError):
            retry(times=0)


class TestCountCalls:
    def test_counts(self):
        @count_calls
        def noop():
            return None

        noop()
        noop()
        noop()
        assert noop.calls == 3


class TestValidateTypes:
    def test_accepts_valid(self):
        @validate_types
        def greet(name: str, times: int) -> str:
            return name * times

        assert greet("ab", 2) == "abab"

    def test_rejects_invalid(self):
        @validate_types
        def greet(name: str, times: int) -> str:
            return name * times

        with pytest.raises(TypeError):
            greet("ab", "2")

    def test_ignores_unannotated(self):
        @validate_types
        def loose(a, b: int):
            return b

        assert loose("anything", 1) == 1

    def test_validates_keyword_arguments(self):
        @validate_types
        def f(a: int = 0):
            return a

        with pytest.raises(TypeError):
            f(a="x")


class TestSingleton:
    def test_same_instance(self):
        @singleton
        class Config:
            def __init__(self):
                self.value = 42

        assert Config() is Config()

    def test_state_shared(self):
        @singleton
        class Counter:
            def __init__(self):
                self.n = 0

        a = Counter()
        a.n = 5
        assert Counter().n == 5
