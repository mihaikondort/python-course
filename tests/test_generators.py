import inspect
import itertools

import pytest

from interview_prep.pythonic.generators import (
    chunked,
    flatten,
    infinite_counter,
    pipeline,
    read_large_file,
    sliding_window,
    take,
    unique,
)


class TestTake:
    def test_takes_n(self):
        assert list(take([1, 2, 3, 4, 5], 3)) == [1, 2, 3]

    def test_fewer_than_n(self):
        assert list(take([1, 2], 5)) == [1, 2]

    def test_zero(self):
        assert list(take([1, 2], 0)) == []

    def test_lazy_on_infinite_input(self):
        assert list(take(itertools.count(), 4)) == [0, 1, 2, 3]

    def test_is_lazy(self):
        consumed = []

        def source():
            for i in range(100):
                consumed.append(i)
                yield i

        list(take(source(), 3))
        assert len(consumed) <= 4


class TestChunked:
    def test_even_chunks(self):
        assert list(chunked([1, 2, 3, 4], 2)) == [[1, 2], [3, 4]]

    def test_ragged_last_chunk(self):
        assert list(chunked([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]

    def test_empty(self):
        assert list(chunked([], 3)) == []

    def test_invalid_size(self):
        with pytest.raises(ValueError):
            list(chunked([1], 0))


class TestFlatten:
    def test_nested(self):
        assert list(flatten([1, [2, [3, [4]]], 5])) == [1, 2, 3, 4, 5]

    def test_strings_are_scalars(self):
        assert list(flatten(["ab", ["cd"]])) == ["ab", "cd"]

    def test_empty(self):
        assert list(flatten([])) == []

    def test_mixed_iterables(self):
        assert list(flatten([1, (2, 3), [4]])) == [1, 2, 3, 4]


class TestUnique:
    def test_preserves_order(self):
        assert list(unique([3, 1, 3, 2, 1])) == [3, 1, 2]

    def test_empty(self):
        assert list(unique([])) == []

    def test_lazy_on_infinite_input(self):
        assert list(take(unique(itertools.cycle([1, 2, 3])), 3)) == [1, 2, 3]


class TestSlidingWindow:
    def test_windows(self):
        assert list(sliding_window([1, 2, 3, 4], 2)) == [(1, 2), (2, 3), (3, 4)]

    def test_input_shorter_than_window(self):
        assert list(sliding_window([1], 3)) == []

    def test_exact_length(self):
        assert list(sliding_window([1, 2], 2)) == [(1, 2)]


class TestInfiniteCounter:
    def test_is_a_generator(self):
        assert inspect.isgenerator(infinite_counter())

    def test_default(self):
        assert list(take(infinite_counter(), 3)) == [0, 1, 2]

    def test_start_and_step(self):
        assert list(take(infinite_counter(10, 5), 3)) == [10, 15, 20]


class TestReadLargeFile:
    def test_batches(self, tmp_path):
        path = tmp_path / "data.txt"
        path.write_text("\n".join(str(i) for i in range(5)), encoding="utf-8")
        assert list(read_large_file(str(path), chunk_lines=2)) == [
            ["0", "1"],
            ["2", "3"],
            ["4"],
        ]

    def test_empty_file(self, tmp_path):
        path = tmp_path / "empty.txt"
        path.write_text("", encoding="utf-8")
        assert list(read_large_file(str(path))) == []


class TestPipeline:
    def test_composes_stages(self):
        def doubled(it):
            return (x * 2 for x in it)

        def positive(it):
            return (x for x in it if x > 0)

        assert list(pipeline([-1, 1, 2], positive, doubled)) == [2, 4]

    def test_no_stages(self):
        assert list(pipeline([1, 2])) == [1, 2]
