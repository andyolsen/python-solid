import abc
from typing import Self

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


# Nope. Can't instantiate shape, because it's an abstract class:
# s = shape(100, 100)