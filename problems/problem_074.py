# Write a class that meets these requirements.
#
# Name:       BankAccount
#
# Required state:
#    * opening balance, the amount of money in the bank account
#
# Behavior:
#    * get_balance()      # Returns how much is in the bank account
#    * deposit(amount)    # Adds money to the current balance
#    * withdraw(amount)   # Reduces the current balance by amount
#
# Example:
#    account = BankAccount(100)
#
#    print(account.get_balance())  # prints 100
#    account.withdraw(50)
#    print(account.get_balance())  # prints 50
#    account.deposit(120)
#    print(account.get_balance())  # prints 170
#
# There is pseudocode for you to guide you.

# class BankAccount
    # method initializer(self, balance)
        # self.balance = balance

    # method get_balance(self)
        # returns the balance

    # method withdraw(self, amount)
        # reduces the balance by the amount

    # method deposit(self, amount)
        # increases the balance by the amount
"""
class practice
SOLVED - 8/13/2022

LESSON:
remember that if you are modifying an attribute, you need to assign the changes 
to the original attribute
self.balance + amount IS NOT self.balance = self.balance + amount
"""


class BankAccount:
    def __init__(self, opening_balance):
        self.balance = opening_balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount


account = BankAccount(100)

print(account.get_balance())  # prints 100
account.withdraw(50)
print(account.get_balance())  # prints 50
account.deposit(120)
print(account.get_balance())  # prints 170