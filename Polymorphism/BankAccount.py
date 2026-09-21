class BankAccount:
    def calculate_interest(self, amount):
        print("Interest")
class SavingsAccount(BankAccount):
    def calculate_interest(self, amount):
        print("Savings Interest:", amount * 0.04)
class CurrentAccount(BankAccount):
    def calculate_interest(self, amount):
        print("Current Interest:", amount * 0.02)
class FixedDepositAccount(BankAccount):
    def calculate_interest(self, amount):
        print("FD Interest:", amount * 0.07)
SavingsAccount().calculate_interest(10000)
CurrentAccount().calculate_interest(10000)
FixedDepositAccount().calculate_interest(10000)