import abc
from math import pi

# Designate shape as an abstract class, by inheriting from abc.ABC.
class shape(abc.ABC):
   
    def __init__(self, cx: int, cy: int):
        self.cx = cx
        self.cy = cy

    # Designate as an abstract method, by annotating with @abc.abstractmethod. 
    @abc.abstractmethod
    def area(self) -> float: 
        raise NotImplementedError("area() not implemented")

    # Designate as an abstract method, by annotating with @abc.abstractmethod. 
    @abc.abstractmethod
    def perimeter(self) -> float: 
        raise NotImplementedError("perimeter() not implemented")


class quadrilateral(shape):

    def __init__(self, cx: int, cy: int, width: int, height: int):
        super().__init__(cx, cy)
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class circle(shape):

    def __init__(self, cx: int, cy: int, radius: int):
        super().__init__(cx, cy)
        self.radius = radius

    def area(self) -> float:
        return pi * self.radius ** 2

    def circumference(self) -> float:
        return 2 * pi * self.radius


# Nope:
# s = shape(100, 100)

# OK:
q = quadrilateral(100, 100, 10, 10)

# Nope:
# c = circle(100, 100, 10)