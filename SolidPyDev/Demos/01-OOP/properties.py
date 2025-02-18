class Employee:

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def name(self):
        return self.__name	

    @name.setter
    def name(self, value):
        self.__name = value	

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value


e1 = Employee("Thomas", 20000)

e1.name = "Tom"
print(e1.name)

e1.salary += 500
print(e1.salary)