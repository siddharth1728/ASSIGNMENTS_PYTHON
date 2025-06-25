# OOPS

class User:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.cart = None

    def add_to_cart(self):
        pass

    def remove_from_cart(self):
        pass


class Product: # this is not the object this is the plan for the object

    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.products = []

user = User("John", 2000)
cart = Cart()
user.cart = cart
user.cart.products.append("Vim")
print(user.cart.products)