# models.py

class Member:
    def __init__(self, name):
        self.name = name
        self.balance = 0.0

    def __repr__(self):
        return f"{self.name}: Balance = {self.balance:.2f}"


class Expense:
    def __init__(self, payer, amount, participants, weights=None):
        self.payer = payer
        self.amount = amount
        self.participants = participants  # list of names
        self.weights = weights  # list of floats or None

    def __repr__(self):
        return f"{self.payer} paid {self.amount} for {self.participants} with weights {self.weights}"
