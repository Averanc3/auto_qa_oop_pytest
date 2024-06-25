from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, a: int | float, b: int | float):
        if (
            not isinstance(a, (int, float))
            or not isinstance(b, (int, float))
            or isinstance(a, bool)
            or isinstance(b, bool)
        ):
            raise ValueError("Sides of rectangle should be a numbers")
        if a <= 0 or b <= 0:
            raise ValueError("Sides should be above 0")
        self.a = a
        self.b = b

    @property
    def get_area(self):
        return self.a * self.b

    @property
    def get_perimeter(self):
        return (self.a + self.b) * 2
