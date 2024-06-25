import pytest

from src.circle import Circle


@pytest.mark.parametrize("type_of_test", ["integer_circle_area", "float_circle_area"])
def test_circle_area_positive(figure_data, type_of_test):
    radius, area = figure_data(type_of_test=type_of_test)
    c = Circle(radius)
    assert (
        c.get_area == area
    ), f"Полученная площадь треугольника {c.get_area} не равна ожидаемой - {area}"


@pytest.mark.parametrize(
    "type_of_test", ["integer_circle_perimeter", "float_circle_perimeter"]
)
def test_circle_perimeter_positive(figure_data, type_of_test):
    radius, perimeter = figure_data(type_of_test=type_of_test)
    print()
    c = Circle(radius)
    assert (
        c.get_perimeter == perimeter
    ), f"Полученный периметр треугольника {c.get_perimeter} не равен ожидаемому - {perimeter}"


@pytest.mark.parametrize("type_of_test", ["boolean", "negative", "zero", "string"])
def test_circle_perimeter_negative(figure_data, type_of_test):
    radius, *extra = figure_data(type_of_test=type_of_test)
    with pytest.raises(ValueError):
        Circle(radius)
