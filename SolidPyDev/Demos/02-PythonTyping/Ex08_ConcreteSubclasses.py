import abc
from typing import Self
from math import pi

# Designate shape as an abstract class, by inheriting from abc.ABC.
class shape(abc.ABC):
   
    def __init__(self: Self, cx: int, cy: int):
        self.cx = cx
        self.cy = cy

    # Designate as an abstract method, by decorating with @abc.abstractmethod. 
    @abc.abstractmethod
    def area(self: Self) -> float:  ...

    # Designate as an abstract method, by decorating with @abc.abstractmethod. 
    @abc.abstractmethod
    def perimeter(self: Self) -> float:  ...


class quadrilateral(shape):

    def __init__(self: Self, cx: int, cy: int, width: int, height: int):
        super().__init__(cx, cy)
        self.width = width
        self.height = height

    def area(self: Self) -> float:
        return self.width * self.height

    def perimeter(self: Self) -> float:
        return 2 * (self.width + self.height)


class circle(shape):

    def __init__(self: Self, cx: int, cy: int, radius: int):
        super().__init__(cx, cy)
        self.radius = radius

    def area(self: Self) -> float:
        return pi * self.radius ** 2

    # Deliberate mistake. This method should have been named perimeter().
    def circumference(self: Self) -> float:
        return 2 * pi * self.radius


# Nope. Can't instantiate shape because it's an abstract class:
# s = shape(100, 100)

# OK:
q = quadrilateral(100, 100, 10, 10)

# Nope. Can't instantiate circle because it doesn't implement perimeter().
# c = circle(100, 100, 10)