from math import sqrt


def calc_discriminant(a: float, b: float, c: float) -> float:
    return b * b - 4 * a * c


def calc_roots(a: float, b: float, c: float) -> tuple[float, float]:
    disc = calc_discriminant(a, b, c)
    if disc < 0:
        raise ValueError("Equation has imaginary roots")
    root1 = (-b + sqrt(disc)) / (2 * a)
    root2 = (-b - sqrt(disc)) / (2 * a)
    return (root1, root2)


def display_squares(*nums: int) -> None:
    for n in nums:
        print(f"{n} squared is {n*n}")


def display_named_squares(**kwargs: int) -> None:
    for k,v in kwargs.items():
        print(f"{k} value squared is {v * v}")


result = calc_roots(1, -3, 2)
print(f"roots are {result[0]} and {result[1]}")
display_squares(3, 19, 2, 5)
display_named_squares(andy=3, jayne=19, em=2, tom=2, andrew=5)