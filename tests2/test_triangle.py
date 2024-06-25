import pytest

from src.triangle import Triangle

@pytest.mark.parametrize("type_of_test",
                         ["integer_triangle_area",
                          "float_triangle_area"])
def test_triangle_area_positive(figure_data, type_of_test):
    side_a, side_b, side_c, area = figure_data(type_of_test=type_of_test)
    t = Triangle(side_a, side_b, side_c)
    assert t.get_area == area, f"Полученная площадь треугольника {t.get_area} не равна ожидаемой - {area}"


@pytest.mark.parametrize("type_of_test",
                         ["integer_triangle_perimeter",
                          "float_triangle_perimeter"])
def test_triangle_perimeter_positive(figure_data, type_of_test):
    side_a, side_b, side_c, perimeter = figure_data(type_of_test=type_of_test)
    print()
    t = Triangle(side_a, side_b, side_c)
    assert t.get_perimeter == perimeter, f"Полученный периметр треугольника {t.get_perimeter} не равен ожидаемому - {perimeter}"


@pytest.mark.parametrize("type_of_test",
                         ["boolean",
                          "negative",
                          "zero",
                          "string",
                          "not_existing_triangle"])
def test_triangle_perimeter_negative(figure_data, type_of_test):
    side_a, side_b, side_c = figure_data(type_of_test=type_of_test)
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)