class BankAccount:
    
    __nextId = 1
    __OVERDRAFT_LIMIT = -1000

    def __init__(self, accountHolder="Anonymous"):
        self.__accountHolder = accountHolder
        self.__balance = 0.0
        self.__id = BankAccount.__nextId
        BankAccount.__nextId += 1

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        newBalance = self.__balance - amount
        if newBalance < BankAccount.__OVERDRAFT_LIMIT:
            raise ValueError(f"Insufficient funds to withdraw {amount}")
        else:
            self.__balance = newBalance
        return self.__balance

    def __str__(self):
        return f"[{self.__id}] {self.__accountHolder}, {self.__balance}"

    @classmethod		
    def getOverdraftLimit(cls):
        return cls.__OVERDRAFT_LIMIT

    @staticmethod		
    def getBanner():
        return "\nThis is the BankAccount Banner"


# client code (invoking methods via class name)
print(BankAccount.getBanner())
print(BankAccount.getOverdraftLimit())
# print("Next ID is %d"         % BankAccount.__nextID)
# print("Overdraft limit is %d" % BankAccount.__OVERDRAFT_LIMIT)