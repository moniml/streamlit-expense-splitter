from models import Member, Expense

class ExpenseSplitter:
    def __init__(self):
        self.members = {}
        self.expenses = []

    def add_member(self, name):
        if name not in self.members:
            self.members[name] = Member(name)

    def add_expense(self, payer, amount, participants):
        if payer not in self.members:
            raise ValueError("Payer not in members.")
        for person in participants:
            if person not in self.members:
                raise ValueError(f"{person} not in members.")

        expense = Expense(payer, amount, participants)
        self.expenses.append(expense)

    def calculate_balances(self):
        # Reset all balances
        for m in self.members.values():
            m.balance = 0.0

        for expense in self.expenses:
            share = expense.amount / len(expense.participants)
            for p in expense.participants:
                self.members[p].balance -= share
            self.members[expense.payer].balance += expense.amount

    def get_settlements(self):
        self.calculate_balances()

        creditors = []
        debtors = []

        for m in self.members.values():
            if m.balance > 0:
                creditors.append([m.name, m.balance])
            elif m.balance < 0:
                debtors.append([m.name, -m.balance])

        settlements = []
        i, j = 0, 0

        while i < len(debtors) and j < len(creditors):
            debtor, debt = debtors[i]
            creditor, credit = creditors[j]

            settled_amount = min(debt, credit)
            settlements.append((debtor, creditor, settled_amount))

            debtors[i][1] -= settled_amount
            creditors[j][1] -= settled_amount

            if debtors[i][1] == 0:
                i += 1
            if creditors[j][1] == 0:
                j += 1

        return settlements
