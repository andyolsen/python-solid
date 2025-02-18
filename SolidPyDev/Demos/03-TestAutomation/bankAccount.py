class BankAccount:

    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise Exception("Insufficient funds")
        self.balance -= amount

    def __str__(self):
        return f"{self.name}, {self.balance}"