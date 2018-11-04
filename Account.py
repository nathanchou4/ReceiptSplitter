# Each person will have an account where we will store:
#   - Name of account holder
#   - Amount of $ that they owe

class Account:
    def __init__(self, name):
        self.account_holder = name
        self.expenses = 0.0

    def add_expense(self, price):
        self.expenses += price
