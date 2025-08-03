from collections import defaultdict
class ExpenseManager:
    def __init__(self):
        self.users = {}
        self.balances = defaultdict(lambda: defaultdict(float))

    def add_user(self, user):
        self.users[user.name] = user

    def add_expense(self, payer_name, amount, participant_names):
        payer = self.users[payer_name]
        participants = [self.users[name] for name in participant_names]
        share = amount / len(participants)

        for participant in participants:
            if participant.name != payer.name:
                self.balances[participant.name][payer.name] += share

    def show_balances(self):  # ✅ This is what you're missing!
        print("\n---- Balances ----")
        no_dues = True
        for user in list(self.balances.keys()):
            for other in list(self.balances[user].keys()):
                amount = self.balances[user][other] - self.balances[other][user]
                if amount > 0:
                    print(f"{user} owes {other}: ${amount:.2f}")
                    no_dues = False
        if no_dues:
            print("All balances are settled.")

