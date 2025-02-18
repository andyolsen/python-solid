from math import pi, hypot


class shape:

    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy

    def area(self):
        raise NotImplementedError("Must implement area()")

    def perimeter(self):
        raise NotImplementedError("Must implement perimeter()")


class circle(shape):

    def __init__(self, cx, cy, radius):
        super().__init__(cx, cy)
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


class quadrilateral(shape):

    def __init__(self, cx, cy, width, height):
        super().__init__(cx, cy)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class right_angled_triangle(shape):

    def __init__(self, cx, cy, base, height):
        super().__init__(cx, cy)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.base + self.height + hypot(self.base, self.height)


def display_info_for_shape(aShape):
    area = aShape.area()
    perimeter = aShape.perimeter()
    print(f"Area of {type(aShape).__name__} is {area:.2f}, perimeter {perimeter:.2f}")


s1 = circle(100, 100, 10)
display_info_for_shape(s1)

s2 = quadrilateral(100, 100, 3, 4)
display_info_for_shape(s2)

s3 = right_angled_triangle(100, 100, 3, 4)
display_info_for_shape(s3)

print("\nHere's a polymorphic collection, contains any kind of shape")
all_my_shapes = [
    circle(100, 100, 10), 
    quadrilateral(100, 100, 3, 4),
    right_angled_triangle(100, 100, 3, 4)
]
for s in all_my_shapes:
    display_info_for_shape(s)