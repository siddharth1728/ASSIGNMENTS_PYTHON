# OOPS

class User:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def add_to_cart(self):
        pass

    def remove_from_cart(self):
        pass

user = User("John", 2000)
user.money = -15000
user2 = User("Alex", 2)
print(f"{user2.name} had {user2.money}")

class Product: # this is not the object this is the plan for the object

    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.products = []

 