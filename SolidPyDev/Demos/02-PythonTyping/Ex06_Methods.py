from typing import Self

class Person:

    def __init__(self: Self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def isOlderThan(self: Self, other: Self) -> bool:
        return self.age > other.age
    

def display_person(p: Person) -> None:
    print(f"{p.name} is {p.age} years old")


person1 = Person("Ola", 30)
person2 = Person("Kari", 29)
display_person(person1)
display_person(person2)
print("Is person1 older than person2?", person1.isOlderThan(person2))