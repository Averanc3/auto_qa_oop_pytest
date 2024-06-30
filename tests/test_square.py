import pytest

from src.square import Square


@pytest.mark.parametrize("type_of_test", ["integer_square_area", "float_square_area"])
def test_rectangle_area_positive(figure_data, type_of_test):
    side_a, area = figure_data(type_of_test=type_of_test)
    print(side_a, area)
    s = Square(side_a)
    assert (
        s.get_area == area
    ), f"Полученная площадь квадрата {s} не равна ожидаемой - {area}"


@pytest.mark.parametrize(
    "type_of_test", ["integer_square_perimeter", "float_square_perimeter"]
)
def test_rectangle_perimeter_positive(figure_data, type_of_test):
    side_a, perimeter = figure_data(type_of_test=type_of_test)
    print(side_a, perimeter)
    r = Square(side_a)
    assert r.get_perimeter == perimeter


@pytest.mark.parametrize("type_of_test", ["boolean", "negative", "zero", "string"])
def test_rectangle_negative(figure_data, type_of_test):
    side_a, *extra = figure_data(type_of_test=type_of_test)
    with pytest.raises(ValueError):
        Square(side_a)
