from math import pi


class shape:

    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy

    def area(self): 
        raise NotImplementedError("area() not implemented")

    def perimeter(self): 
        raise NotImplementedError("perimeter() not implemented")


class quadrilateral(shape):

    def __init__(self, cx, cy, width, height):
        super().__init__(cx, cy)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class circle(shape):

    def __init__(self, cx, cy, radius):
        super().__init__(cx, cy)
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def circumference(self):    # oops, spot the bug 🤪
        return 2 * pi * self.radius