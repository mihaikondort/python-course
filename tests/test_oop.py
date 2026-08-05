import pytest

from interview_prep.pythonic.oop import (
    Circle,
    Rectangle,
    Shape,
    Stack,
    Temperature,
    TypedField,
    Vector,
)


class TestVector:
    def test_add_and_sub(self):
        assert Vector(1, 2) + Vector(3, 4) == Vector(4, 6)
        assert Vector(3, 4) - Vector(1, 2) == Vector(2, 2)

    def test_scalar_multiplication_both_sides(self):
        assert Vector(1, 2) * 3 == Vector(3, 6)
        assert 3 * Vector(1, 2) == Vector(3, 6)

    def test_abs(self):
        assert abs(Vector(3, 4)) == 5

    def test_repr_round_trips(self):
        v = Vector(1, 2)
        assert eval(repr(v)) == v  # noqa: S307

    def test_hashable(self):
        assert len({Vector(1, 2), Vector(1, 2), Vector(3, 4)}) == 2

    def test_iter_and_len(self):
        assert list(Vector(1, 2)) == [1, 2]
        assert len(Vector(1, 2)) == 2

    def test_bool(self):
        assert bool(Vector(0, 0)) is False
        assert bool(Vector(0, 1)) is True

    def test_not_equal_to_other_types(self):
        assert Vector(1, 2) != (1, 2)


class TestTemperature:
    def test_conversion(self):
        assert Temperature(100).fahrenheit == pytest.approx(212)
        assert Temperature(0).fahrenheit == pytest.approx(32)

    def test_fahrenheit_setter(self):
        t = Temperature(0)
        t.fahrenheit = 212
        assert t.celsius == pytest.approx(100)

    def test_from_fahrenheit(self):
        assert Temperature.from_fahrenheit(32).celsius == pytest.approx(0)

    def test_below_absolute_zero_rejected(self):
        with pytest.raises(ValueError):
            Temperature(-300)

    def test_setter_validates(self):
        t = Temperature(0)
        with pytest.raises(ValueError):
            t.celsius = -300


class TestShapes:
    def test_abstract_cannot_instantiate(self):
        with pytest.raises(TypeError):
            Shape()

    def test_circle(self):
        c = Circle(2)
        assert c.area() == pytest.approx(12.566370, rel=1e-5)
        assert c.perimeter() == pytest.approx(12.566370, rel=1e-5)

    def test_rectangle(self):
        r = Rectangle(2, 3)
        assert r.area() == 6
        assert r.perimeter() == 10

    def test_describe_uses_subclass(self):
        assert "6" in Rectangle(2, 3).describe()

    def test_negative_dimensions_rejected(self):
        with pytest.raises(ValueError):
            Circle(-1)
        with pytest.raises(ValueError):
            Rectangle(-1, 2)


class TestTypedField:
    @pytest.fixture
    def person_class(self):
        class Person:
            name = TypedField(str)
            age = TypedField(int)

            def __init__(self, name, age):
                self.name = name
                self.age = age

        return Person

    def test_accepts_correct_types(self, person_class):
        p = person_class("Ada", 36)
        assert p.name == "Ada"
        assert p.age == 36

    def test_rejects_wrong_type(self, person_class):
        with pytest.raises(TypeError):
            person_class("Ada", "36")

    def test_instances_do_not_share_state(self, person_class):
        a = person_class("Ada", 36)
        b = person_class("Bob", 40)
        assert a.name == "Ada"
        assert b.name == "Bob"


class TestStack:
    def test_lifo(self):
        s = Stack()
        s.push(1)
        s.push(2)
        assert s.pop() == 2
        assert s.pop() == 1

    def test_peek_does_not_remove(self):
        s = Stack()
        s.push(1)
        assert s.peek() == 1
        assert len(s) == 1

    def test_pop_empty_raises(self):
        with pytest.raises(IndexError):
            Stack().pop()

    def test_bool_and_contains(self):
        s = Stack()
        assert bool(s) is False
        s.push("a")
        assert bool(s) is True
        assert "a" in s
        assert "b" not in s
