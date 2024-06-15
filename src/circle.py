from src.figure import Figure
from math import pi


class Circle(Figure):
    def __init__(self, r: float):
        if not isinstance(r, (int, float)):
            raise ValueError("Radius should be a number")
        if r <= 0:
            raise ValueError("Radius should be above 0")
        self.r = r

    @property
    def get_area(self):
        return pi * self.r**2

    @property
    def get_perimeter(self):
        return 2 * pi * self.r
