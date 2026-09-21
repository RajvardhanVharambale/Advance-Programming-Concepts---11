class FoodOrder:
    def __init__(self, order_id, name, food, quantity, price):
        self.order_id = order_id
        self.name = name
        self.food = food
        self.quantity = quantity
        self.price = price
    def total_bill(self):
        total = self.quantity * self.price
        tax = total * 0.05
        return total + tax
    def display(self):
        print("Order ID:", self.order_id)
        print("Customer:", self.name)
        print("Food:", self.food)
        print("Quantity:", self.quantity)
        print("Price:", self.price)
        print("Total Bill:", self.total_bill())
    def __del__(self):
        print("Order completed")
order = FoodOrder(101, "Maddy", "Pizza", 2, 300)
order.display()
del order