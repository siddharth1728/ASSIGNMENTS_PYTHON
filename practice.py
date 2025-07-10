

class User:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.cart = None

    def add_to_cart(self):
        pass

    def  remove_from_cart(self):
        pass

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        