import pytest


@pytest.fixture
def figure_data(request):
    print("\nStart API")

    def _wrapper(type_of_test: str):
        """Circle positive tests"""
        if type_of_test == "integer_circle_area":
            return 6, 113.1
        if type_of_test == "float_circle_area":
            return 4.5, 63.62
        if type_of_test == "integer_circle_perimeter":
            return 20, 125.66
        if type_of_test == "float_circle_perimeter":
            return 6.5, 40.84

        """Triangle positive tests"""
        if type_of_test == "integer_triangle_area":
            return 3, 4, 5, 6
        if type_of_test == "float_triangle_area":
            return 4.5, 5.7, 4.2, 9.35
        if type_of_test == "integer_triangle_perimeter":
            return 7, 4, 8, 19
        if type_of_test == "float_triangle_perimeter":
            return 3.5, 2.2, 4.2, 9.9

        """Square positive tests"""
        if type_of_test == "integer_square_area":
            return 7, 49
        if type_of_test == "float_square_area":
            return 4.5, 20.25
        if type_of_test == "integer_square_perimeter":
            return 3, 12
        if type_of_test == "float_square_perimeter":
            return 5.5, 22

        """Rectangle positive tests"""
        if type_of_test == "integer_rectangle_area":
            return 3, 5, 15
        if type_of_test == "float_rectangle_area":
            return 3.5, 5.5, 19.25
        if type_of_test == "integer_rectangle_perimeter":
            return 3, 5, 16
        if type_of_test == "float_rectangle_perimeter":
            return 3.5, 5.5, 18

        """negative tests"""
        if type_of_test == "boolean":
            return True, False, 4
        if type_of_test == "negative":
            return -4, -5, 4
        if type_of_test == "zero":
            return 0, 7, 0
        if type_of_test == "string":
            return "5", "7", 2
        if type_of_test == "not_existing_triangle":
            return 4, 5, 20

    yield _wrapper
    print("\nEnd API")
