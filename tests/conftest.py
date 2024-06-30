import pytest


@pytest.fixture
def figure_data(request):
    print("\nStart test")

    data = {
        "integer_circle_area": (6, 113.1),
        "float_circle_area": (4.5, 63.62),
        "integer_circle_perimeter": (20, 125.66),
        "float_circle_perimeter": (6.5, 40.84),
        "integer_triangle_area": (3, 4, 5, 6),
        "float_triangle_area": (4.5, 5.7, 4.2, 9.35),
        "integer_triangle_perimeter": (7, 4, 8, 19),
        "float_triangle_perimeter": (3.5, 2.2, 4.2, 9.9),
        "integer_square_area": (7, 49),
        "float_square_area": (4.5, 20.25),
        "integer_square_perimeter": (3, 12),
        "float_square_perimeter": (5.5, 22),
        "integer_rectangle_area": (3, 5, 15),
        "float_rectangle_area": (3.5, 5.5, 19.25),
        "integer_rectangle_perimeter": (3, 5, 16),
        "float_rectangle_perimeter": (3.5, 5.5, 18),
        "boolean": (True, False, 4),
        "negative": (-4, -5, 4),
        "zero": (0, 7, 0),
        "string": ("5", "7", 2),
        "not_existing_triangle": (4, 5, 20),
    }

    def _wrapper(type_of_test: str):
        return data.get(type_of_test)

    yield _wrapper
    print("\nEnd test")
