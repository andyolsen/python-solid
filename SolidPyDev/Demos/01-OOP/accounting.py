class BankAccount:

    def __init__(self, accountHolder="Anonymous"):
        self.__accountHolder = accountHolder
        self.__balance = 0.0

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        self.__balance -= amount
        return self.__balance

    def __str__(self):
        return f"{self.__accountHolder}, {self.__balance}"