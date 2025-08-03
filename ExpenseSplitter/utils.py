def print_members(members):
    print("\nGroup Members:")
    for name in members:
        print(f"- {name}")

def print_balances(members):
    print("\nFinal Balances:")
    for name, member in members.items():
        print(f"{name}: {member.balance:.2f}")

def print_settlements(settlements):
    print("\nSettlement Suggestions:")
    for debtor, creditor, amount in settlements:
        print(f"{debtor} pays {creditor}: {amount:.2f}")

