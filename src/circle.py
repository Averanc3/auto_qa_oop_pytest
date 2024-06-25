from src.figure import Figure
from math import pi


class Circle(Figure):
    def __init__(self, r: int | float):
        if not isinstance(r, (int, float)) or isinstance(r, bool):
            raise ValueError("Radius should be a number")
        if r <= 0:
            raise ValueError("Radius should be above 0")
        self.r = r

    @property
    def get_area(self):
        return round((pi * self.r**2), 2)

    @property
    def get_perimeter(self):
        return round((2 * pi * self.r), 2)

