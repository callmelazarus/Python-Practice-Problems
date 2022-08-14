# Modify the withdraw method of BankAccount so that the bank
# account can not have a negative balance.
#
# If a person tries to withdraw more than what is in the
# balance, then the method should raise a ValueError.

"""
class practice
SOLVED - 8/13/2022

LESSON:
consider edge cases that are logical
"""
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        # If the amount is more than what is in
        # the balance, then raise a ValueError
        self.balance -= amount
        if self.balance < 0:
            raise ValueError

    def deposit(self, amount):
        self.balance += amount
