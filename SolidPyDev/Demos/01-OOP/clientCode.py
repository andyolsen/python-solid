from accounting import BankAccount

# Create and use objects.
acc1 = BankAccount()
acc2 = BankAccount("Bond")

# Invoke methods on objects.
acc1.deposit(200)
acc1.withdraw(50)
# acc1.__balance += 1000000
print(acc1)