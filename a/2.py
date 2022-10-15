from fractions import Fraction


class Rational:
    def __init__(self, first: int = 1, second: int = 1):
        if not isinstance(first, int):
            raise TypeError
        if not isinstance(second, int):
            raise TypeError
        self.__a = Fraction(first, second)

    def divide_view(self):
        print(self.__a)

    def point_view(self):
        print(self.__a.numerator / self.__a.denominator)


a = Rational(25, 100)
a.divide_view()
a.point_view()
