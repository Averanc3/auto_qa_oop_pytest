import pytest

from src.rectangle import Rectangle


@pytest.mark.parametrize(
    "type_of_test", ["integer_rectangle_area", "float_rectangle_area"]
)
def test_rectangle_area_positive(figure_data, type_of_test):
    side_a, side_b, area = figure_data(type_of_test=type_of_test)
    print(side_a, side_b, area)
    r = Rectangle(side_a, side_b)
    assert r.get_area == area


@pytest.mark.parametrize(
    "type_of_test", ["integer_rectangle_perimeter", "float_rectangle_perimeter"]
)
def test_rectangle_perimeter_positive(figure_data, type_of_test):
    side_a, side_b, perimeter = figure_data(type_of_test=type_of_test)
    print(side_a, side_b, perimeter)
    r = Rectangle(side_a, side_b)
    assert r.get_perimeter == perimeter


@pytest.mark.parametrize("type_of_test", ["boolean", "negative", "zero", "string"])
def test_rectangle_negative(figure_data, type_of_test):
    side_a, side_b, *extra = figure_data(type_of_test=type_of_test)
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)
