from typing import Self, Type


class Person:

    def __init__(self: Self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def display(self: Self) -> None:
        print("I am a person")
    

class Student(Person):
    
    def __init__(self: Self, name: str, age: int) -> None:
        super().__init__(name, age)

    def display(self: Self) -> None:
        print("I am a student")


class Employee(Person):
    
    def __init__(self: Self, name: str, age: int) -> None:
        super().__init__(name, age)

    def display(self: Self) -> None:
        print("I am an employee")


def create_kind_of_person(cls: Type[Person], name: str, age: int) -> Person:
    if age > 125:
        raise ValueError("How old???")
    return cls(name, age)


def display_some_kind_of_person(p: Person) -> None:
    p.display()


p1 = create_kind_of_person(Student, "William", 20)
p2 = create_kind_of_person(Employee, "Kate", 30)
display_some_kind_of_person(p1)
display_some_kind_of_person(p2)