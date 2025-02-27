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

class Coupon:
    def __init__(self, code, discount):
        self.code = code
        self.discount = discount

coupon1 = Coupon("code1", 0.8)
coupon2 = Coupon("code2", 0.7)
coupon3 = Coupon("code3", 0.9)


item1 = CartItem("Phone", 50000, 2)
item2 = CartItem("Computer", 70000, 1)
item3 = CartItem("Book", 500, 2)

class ShoppingCart:
    coupon_list = [coupon1, coupon2, coupon3]

    def __init__(self, listing):
        self.listing = listing
    
    def add_item(self, item):
        self.listing.append(item)

    def display_items(self):
        for i in self.listing:
            print(f"{i.name} {i.price}")
    
    def calculate_totals(self):
        return sum([item.calculate_total() for item in self.listing])
    
    def remove_item(self, cart_item):
        self.listing = [item for item in self.listing if item != cart_item]

    def clear(self):
        self.listing = []

    @classmethod
    def get_coupons(cls):
        return [coupon.code for coupon in cls.coupon_list]
    
    @classmethod
    def get_coupon(cls, code):
        return next(filter(lambda coupon: coupon.code == code, ShoppingCart.coupon_list))
    
    def apply_coupon(self, code):
        if code not in ShoppingCart.get_coupons():
            raise ValueError(f"invalid coupon code: {code}")
        
        coupon = ShoppingCart.get_coupon(code)

        for index in range(0, len(self.listing)):
            self.listing[index].price = self.listing[index].price * coupon.discount

shopping_cart = ShoppingCart([item1, item2])

shopping_cart.add_item(item3)
shopping_cart.display_items()

print(shopping_cart.calculate_totals())

# shopping_cart.remove_item(item1)
# shopping_cart.display_items()

# shopping_cart.clear()
# shopping_cart.display_items()

shopping_cart.apply_coupon("code2")
print(shopping_cart.calculate_totals())