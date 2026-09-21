class ShoppingCart:
    def __init__(self, name, cart_id):
        self.name = name
        self.cart_id = cart_id
        self.products = []
    def add_product(self, product, price):
        self.products.append((product, price))
        print(product, "added")
    def remove_product(self, product):
        for item in self.products:
            if item[0] == product:
                self.products.remove(item)
                print(product, "removed")
                return
        print("Product not found")
    def total_bill(self):
        total = 0
        for item in self.products:
            total += item[1]
        return total
    def __del__(self):
        print("Shopping cart destroyed")
cart = ShoppingCart("Paddy", 101)
cart.add_product("Mobile", 20000)
cart.add_product("Headphones", 2000)
cart.add_product("Mouse", 1000)
cart.remove_product("Mouse")
print("Customer:", cart.name)
print("Cart ID:", cart.cart_id)
print("Total Bill:", cart.total_bill())
del cart