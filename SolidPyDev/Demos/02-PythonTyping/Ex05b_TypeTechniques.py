from typing import Callable


def apply(a: int, b: int, op: Callable[[int,int], int]) -> int :
    print("In apply()")
    return op(a, b)


res1 = apply(10, 20, lambda x, y: x + y)
print(res1)

res2 = apply(10, 20, lambda x, y: x - y)
print(res2)

res3 = apply(10, 20, lambda x, y: x * y)
print(res3)