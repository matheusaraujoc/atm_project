class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance