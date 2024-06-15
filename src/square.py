from src.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, a: float):
        if not isinstance(a, (int, float)):
            raise ValueError("Square side should be a number")
        if a <= 0:
            raise ValueError("Side should be above 0")
        super().__init__(a, a)

        self.a = a
