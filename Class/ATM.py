class ATM:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance
    def check_balance(self):
        print("Balance:", self.balance)
    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient Balance")
    def account_details(self):
        print("Account No:", self.account_no)
        print("Name:", self.name)
        print("Balance:", self.balance)
a = ATM(1001, "Jonny", 10000)
while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Account Details")
    print("5. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        a.check_balance()
    elif choice == 2:
        amount = float(input("Enter amount: "))
        a.deposit(amount)
    elif choice == 3:
        amount = float(input("Enter amount: "))
        a.withdraw(amount)
    elif choice == 4:
        a.account_details()
    elif choice == 5:
        print("Thank You")
        break
    else:
        print("Invalid Choice")