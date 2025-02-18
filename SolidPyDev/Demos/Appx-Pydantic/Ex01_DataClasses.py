from dataclasses import dataclass


# Here's a class, defined as a dataclass.
@dataclass
class person_as_dataclass:
    name: str
    age: int


# Equivalent as a vanilla class.
class person_as_vanilla_class:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
         return f"{type(self).__name__}(name={self.name}, age={self.age})"

    def __eq__(self, other):
         if other.__class__ is not self.__class__:
             return NotImplemented
         else:
             return (self.name, self.age) == (other.name, other.age)


p1 = person_as_dataclass("Jayne", 60) 
p2 = person_as_dataclass("Andy", 60)
print(p1)
print(p2)
print(p1 == p2)

p3 = person_as_vanilla_class("Emily", 27) 
p4 = person_as_vanilla_class("Thomas", 27)
print(p3)
print(p4)
print(p3 == p4)