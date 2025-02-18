from math import pi, hypot


class shape:

    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy


class circle(shape):

    def __init__(self, cx, cy, radius):
        super().__init__(cx, cy)
        self.radius = radius


class quadrilateral(shape):

    def __init__(self, cx, cy, width, height):
        super().__init__(cx, cy)
        self.width = width
        self.height = height


class right_angled_triangle(shape):

    def __init__(self, cx, cy, base, height):
        super().__init__(cx, cy)
        self.base = base
        self.height = height


def display_info_for_shape(aShape):

    if isinstance(aShape, circle):
        area = pi * aShape.radius ** 2
        perimeter = 2 * pi * aShape.radius

    elif isinstance(aShape, quadrilateral):
        area = aShape.width * aShape.height
        perimeter = 2 * (aShape.width + aShape.height)

    elif isinstance(aShape, right_angled_triangle):
        area = 0.5 * aShape.base * aShape.height
        perimeter = aShape.base + aShape.height + hypot(aShape.base, aShape.height)

    else:
        raise TypeError("Not a shape!")
    
    print(f"Area of {type(aShape).__name__} is {area:.2f}, perimeter {perimeter:.2f}")


s1 = circle(100, 100, 10)
display_info_for_shape(s1)

s2 = quadrilateral(100, 100, 3, 4)
display_info_for_shape(s2)

s3 = right_angled_triangle(100, 100, 3, 4)
display_info_for_shape(s3)