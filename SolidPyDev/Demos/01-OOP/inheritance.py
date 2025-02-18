class BankAccount:

    __nextId = 1
    __OVERDRAFT_LIMIT = -1000

    def __init__(self, accountHolder="Anonymous"):
        self.accountHolder = accountHolder
        self.balance = 0.0
        self.id = BankAccount.__nextId
        BankAccount.__nextId += 1

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        newBalance = self.balance - amount
        if newBalance < BankAccount.__OVERDRAFT_LIMIT:
            raise ValueError(f"Insufficient funds to withdraw {amount}")
        else:
            self.balance = newBalance
        return self.balance

    def __str__(self):
        return f"[{self.id}] {self.accountHolder}, balance {self.balance}"

    @classmethod		
    def getOverdraftLimit(cls):
        return cls.__OVERDRAFT_LIMIT


class SavingsAccount(BankAccount):

    def __init__(self, accountHolder="Anonymous", interestRate=0.0):
        super().__init__(accountHolder)
        self.interestRate = interestRate
            
    def earnInterest(self):
        self.balance *= (1 + self.interestRate)
        return self.balance 

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("You can't go overdrawn in a savings account")
        else:
            super().withdraw(amount)
        return self.balance

    def __str__(self):
        baseStr = super().__str__()
        return f"{baseStr}, interest rate {self.interestRate}"
    

acc1 = SavingsAccount("Gareth", 0.20)
acc1.deposit(100)
acc1.earnInterest()
acc1.withdraw(25)
print(acc1)