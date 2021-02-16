from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calc_area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        self.area = 0

    def calc_area(self):
        self.area = self.length * self.breadth

    def __str__(self):
        return f"The Area of Rectangle is: {self.area}"


# We can't create object of abstract class
# shape = Shape()

rect = Rectangle(5, 10)
rect.calc_area()
print(rect)