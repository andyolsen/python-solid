from typing import Self

class Employee:

    def __init__(self: Self, name: str, id: int, salary: int) -> None:
        self.name = name
        self.id = id
        self.salary = salary

    def __str__(self: Self) -> str:
        return f"[{self.id} {self.name}, earns {self.salary} ]"
    

emp1 = Employee("Mary", 1, 10000)
emp2 = Employee("Mungo", 2, 20000)
emp3 = Employee("Midge", 30000, 3)