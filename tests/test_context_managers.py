from pathlib import Path

import pytest

from interview_prep.pythonic.context_managers import (
    Timer,
    atomic_write,
    suppress_errors,
    temporary_attribute,
    working_directory,
)


class TestTimer:
    def test_measures(self):
        with Timer() as t:
            sum(range(1000))
        assert t.elapsed >= 0

    def test_records_even_on_exception(self):
        timer = Timer()
        with pytest.raises(ValueError), timer:
            raise ValueError("boom")
        assert timer.elapsed >= 0


class TestSuppressErrors:
    def test_suppresses_listed(self):
        with suppress_errors(ValueError) as ctx:
            raise ValueError("caught")
        assert isinstance(ctx.exception, ValueError)

    def test_propagates_unlisted(self):
        with pytest.raises(TypeError), suppress_errors(ValueError):
            raise TypeError("not caught")

    def test_no_exception(self):
        with suppress_errors(ValueError) as ctx:
            pass
        assert ctx.exception is None

    def test_multiple_types(self):
        with suppress_errors(ValueError, KeyError) as ctx:
            raise KeyError("k")
        assert isinstance(ctx.exception, KeyError)


class TestAtomicWrite:
    def test_writes_on_success(self, tmp_path):
        target = tmp_path / "out.txt"
        with atomic_write(target) as f:
            f.write("hello")
        assert target.read_text(encoding="utf-8") == "hello"

    def test_leaves_original_on_failure(self, tmp_path):
        target = tmp_path / "out.txt"
        target.write_text("original", encoding="utf-8")
        with pytest.raises(RuntimeError), atomic_write(target) as f:
            f.write("partial")
            raise RuntimeError("boom")
        assert target.read_text(encoding="utf-8") == "original"

    def test_no_temp_files_left_behind(self, tmp_path):
        target = tmp_path / "out.txt"
        with atomic_write(target) as f:
            f.write("x")
        assert [p.name for p in tmp_path.iterdir()] == ["out.txt"]


class TestTemporaryAttribute:
    def test_restores_existing(self):
        class Obj:
            value = 1

        obj = Obj()
        with temporary_attribute(obj, "value", 99):
            assert obj.value == 99
        assert obj.value == 1

    def test_removes_when_absent_before(self):
        class Obj:
            pass

        obj = Obj()
        with temporary_attribute(obj, "temp", 5):
            assert obj.temp == 5
        assert not hasattr(obj, "temp")

    def test_restores_on_exception(self):
        class Obj:
            value = 1

        obj = Obj()
        with pytest.raises(RuntimeError), temporary_attribute(obj, "value", 99):
            raise RuntimeError("boom")
        assert obj.value == 1


class TestWorkingDirectory:
    def test_changes_and_restores(self, tmp_path):
        before = Path.cwd()
        with working_directory(tmp_path):
            assert Path.cwd().resolve() == tmp_path.resolve()
        assert Path.cwd() == before

    def test_restores_on_exception(self, tmp_path):
        before = Path.cwd()
        with pytest.raises(RuntimeError), working_directory(tmp_path):
            raise RuntimeError("boom")
        assert Path.cwd() == before
