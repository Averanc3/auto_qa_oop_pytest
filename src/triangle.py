from src.figure import Figure


class Triangle(Figure):
    def __init__(self, a: int | float, b: int | float, c: int | float):
        for i in (a, b, c):
            if not isinstance(i, (int, float)) or isinstance(i, bool):
                raise ValueError("Sides of triangle should be a numbers")
        if a <= 0 or b <= 0:
            raise ValueError("Sides should be above 0")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("The triangle with sides given doesn't exist")
        self.a = a
        self.b = b
        self.c = c

    @property
    def get_area(self):
        p = (self.a + self.b + self.c) / 2
        return round(((p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5), 2)

    @property
    def get_perimeter(self):
        return round((self.a + self.b + self.c), 2)
