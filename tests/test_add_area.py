import pytest

from src.square import Square
from src.rectangle import Rectangle
from src.circle import Circle
from src.triangle import Triangle

t = Triangle(3, 4, 5)
c = Circle(4)
s = Square(10)
r = Rectangle(6, 8)


@pytest.mark.parametrize(
    "type_of_test", ["integer_triangle_area", "float_triangle_area"]
)
def test_triangle_add_area_positive(figure_data, type_of_test):
    side_a, side_b, side_c, area = figure_data(type_of_test=type_of_test)
    t1 = Triangle(side_a, side_b, side_c)
    for figure in (t, c, s, r):
        print(t1.add_figure(figure))
        assert (
            t1.add_figure(figure) == figure.get_area + t1.get_area
        ), f"Полученная сумма площадей фигур {t1.add_figure(figure)} не равна ожидаемой - {figure.get_area + t1.get_area}"


@pytest.mark.parametrize(
    "type_of_test", ["integer_rectangle_area", "float_rectangle_area"]
)
def test_rectangle_add_area_positive(figure_data, type_of_test):
    side_a, side_b, area = figure_data(type_of_test=type_of_test)
    r1 = Rectangle(side_a, side_b)
    for figure in (t, c, s, r):
        print(r1.add_figure(figure))
        assert (
            r1.add_figure(figure) == figure.get_area + r1.get_area
        ), f"Полученная сумма площадей фигур {r1.add_figure(figure)} не равна ожидаемой - {figure.get_area + r1.get_area}"


@pytest.mark.parametrize("type_of_test", ["integer_square_area", "float_square_area"])
def test_square_add_area_positive(figure_data, type_of_test):
    side_a, area = figure_data(type_of_test=type_of_test)
    s1 = Square(side_a)
    for figure in (t, c, s, r):
        print(s1.add_figure(figure))
        assert (
            s1.add_figure(figure) == figure.get_area + s1.get_area
        ), f"Полученная сумма площадей фигур {s1.add_figure(figure)} не равна ожидаемой - {figure.get_area + s1.get_area}"


@pytest.mark.parametrize("type_of_test", ["integer_circle_area", "float_circle_area"])
def test_circle_add_area_positive(figure_data, type_of_test):
    side_a, area = figure_data(type_of_test=type_of_test)
    c1 = Circle(side_a)
    for figure in (t, c, s, r):
        print(c1.add_figure(figure))
        assert (
            c1.add_figure(figure) == figure.get_area + c1.get_area
        ), f"Полученная сумма площадей фигур {c1.add_figure(figure)} не равна ожидаемой - {figure.get_area + c1.get_area}"


@pytest.mark.parametrize(
    "type_of_test",
    [
        "boolean",
        "negative",
        "zero",
        "string",
        "integer_circle_area",
        "float_circle_area",
    ],
)
def test_circle_perimeter_negative(figure_data, type_of_test):
    value, *extra = figure_data(type_of_test=type_of_test)
    for figure in (t, c, s, r):
        with pytest.raises(ValueError):
            print(f"{value} and {figure}")
            figure.add_figure(value)
