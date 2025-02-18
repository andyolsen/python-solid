from typing import overload

@overload
def seconds_to_midnight(p1: int) -> int: 
    """p1 is the number of seconds since midnight"""
    ...


@overload
def seconds_to_midnight(p1: int, p2: int, p3: int) -> int: 
    """p1, p2, p3 are the hours, minutes, seconds"""
    ...


def seconds_to_midnight(
        p1: int, 
        p2: int | None = None, 
        p3: int | None = None) -> int:

    NUM_SECS_IN_DAY = 60*60*24

    if (p2 is None or p3 is None):
        return NUM_SECS_IN_DAY - p1
    else:
        return NUM_SECS_IN_DAY - (p1*60*60 + p2*60 + p3)


res1 = seconds_to_midnight(86_395)  # == 11.59:55pm 
res2 = seconds_to_midnight(23, 59, 57)

print(f"result1: {res1} seconds to midnight")
print(f"result2: {res2} seconds to midnight")