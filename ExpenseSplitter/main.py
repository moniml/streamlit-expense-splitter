from splitter import ExpenseSplitter
from utils import print_members, print_balances, print_settlements
from pipeline import Pipeline

def collect_members(splitter):
    count = int(input("Enter number of members: "))
    for _ in range(count):
        name = input("Enter member name: ")
        splitter.add_member(name)
    return splitter

def collect_expenses(splitter):
    while True:
        payer = input("\nEnter payer name (or 'done' to finish): ")
        if payer.lower() == 'done':
            break
        amount = float(input("Enter amount paid: "))
        participants = input("Enter participants (comma-separated): ").split(",")
        participants = [p.strip() for p in participants]
        splitter.add_expense(payer, amount, participants)
    return splitter

def display_results(splitter):
    settlements = splitter.get_settlements()
    print_balances(splitter.members)
    print_settlements(settlements)

def main():
    splitter = ExpenseSplitter()
    pipeline = Pipeline()
    pipeline.add_step(collect_members)
    pipeline.add_step(collect_expenses)
    pipeline.add_step(display_results)
    pipeline.run(splitter)

if __name__ == "__main__":
    main()
