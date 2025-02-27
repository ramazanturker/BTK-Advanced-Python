class CartItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

item1 = CartItem("Phone", 50000, 2)
item2 = CartItem("Computer", 70000, 1)
item3 = CartItem("Book", 200, 2)