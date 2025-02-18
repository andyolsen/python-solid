from typing import Self, NewType

# Invent new types, which effectively inherit from int in both cases (but are NOT actually int).
# These are distinct types, as far as a static type checker is concerned. They're not just aliases for int.
Money = NewType('Money', int)
PK = NewType('PK', int)

class Employee:

    def __init__(self: Self, name: str, id: PK, salary: Money) -> None:
        self.name = name
        self.id = id
        self.salary = salary

    def __str__(self: Self) -> str:
        return f"[{self.id} {self.name}, earns {self.salary} ]"
    

emp1 = Employee("Mary",  PK(1), Money(10000))
emp2 = Employee("Mungo", PK(2), Money(20000))
emp3 = Employee("Midge", PK(3), Money(30000))