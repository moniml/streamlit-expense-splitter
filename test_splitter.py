from ExpenseSplitter.splitter import ExpenseSplitter

def test_basic_split():
    s = ExpenseSplitter()
    s.add_member("Alice")
    s.add_member("Bob")
    s.add_member("Charlie")

    s.add_expense("Alice", 90, ["Alice", "Bob", "Charlie"])
    s.add_expense("Bob", 60, ["Alice", "Bob"])
    
    settlements = s.get_settlements()
    for line in settlements:
        print(line)

if __name__ == "__main__":
    test_basic_split()
