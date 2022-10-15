class Rectangle:

    def __init__(self, length: int | float = 1, width: int | float = 1):
        self.set_info(length, width)

    def show_length(self):
        return self.__length

    def show_width(self):
        return self.__width

    def set_info(self, length, width):
        if not isinstance(length, int | float):
            raise TypeError
        if not isinstance(width, int | float):
            raise TypeError
        if length < 0 or length > 20:
            self.__length = 1
        else: self.__length = length
        if width < 0 or width > 20:
            self.__width = 1
        else: self.__width = width

    def perimeter(self):
        return (self.__length + self.__width) * 2

    def area(self):
        return self.__length * self.__width

a = Rectangle(5,6)
print(a.show_length(), a.show_width())
print("Perimeter =", a.perimeter())
print("Area =", a.area())
