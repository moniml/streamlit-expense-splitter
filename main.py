from models import User
from manager import ExpenseManager
from utils import prompt_user_list

def main():
    print("===== Expense Splitter =====")
    manager = ExpenseManager()

    # Add users
    user_names = prompt_user_list()
    for name in user_names:
        manager.add_user(User(name))

    while True:
        print("\nOptions:")
        print("1. Add an expense")
        print("2. Show balances")
        print("3. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            payer = input("Enter payer name: ").strip()
            amount = float(input("Enter amount paid: "))
            participants = input("Enter participants (comma-separated): ").strip().split(',')
            participants = [name.strip() for name in participants]
            manager.add_expense(payer, amount, participants)
        elif choice == '2':
            manager.show_balances()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()


