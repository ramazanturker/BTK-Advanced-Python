class CartItem:
    discount_rate = 0.8
    item_count = 0

    @classmethod
    def display_item_count(cls):
        return f"{cls.item_count} pieces products created"
    
    @classmethod
    def create_item(cls, data_str):
        name, price, quantity = data_str.split(",")
        return cls(name, price, quantity)

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        CartItem.item_count += 1
    
    def calculate_total(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * CartItem.discount_rate

print(CartItem.display_item_count())

item1 = CartItem("Phone", 50000, 2)
item2 = CartItem("Computer", 70000, 1)
item3 = CartItem("Book", 200, 2)
item4 = CartItem("Book", 200, 2)

CartItem.create_item("Mouse, 800, 3")

print(CartItem.display_item_count())