class User:
    def __init__(self, name):
        self.name = name

class Expense:
    def __init__(self, payer, amount, participants):
        self.payer = payer
        self.amount = amount
        self.participants = participants
