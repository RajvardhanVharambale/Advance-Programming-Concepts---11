class Payment:
    def make_payment(self, amount):
        print("Making Payment")
class UPIPayment(Payment):
    def make_payment(self, amount):
        print("UPI Payment:", amount)
class CardPayment(Payment):
    def make_payment(self, amount):
        print("Card Payment:", amount)
class WalletPayment(Payment):
    def make_payment(self, amount):
        print("Wallet Payment:", amount)
def pay(payment, amount):
    payment.make_payment(amount)
pay(UPIPayment(), 1000)
pay(CardPayment(), 2000)
pay(WalletPayment(), 500)