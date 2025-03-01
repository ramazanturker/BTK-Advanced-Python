class Product:
    def __init__(self, name, price):
        self.name = name
        if price >= 0:
            self._price = price
        else:
            raise ValueError("cannot assign negative value for product price")

    @property    
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("cannot assign negative value for product price")

    """
        # other method
        def set_price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("cannot assign negative value for product price")

        def get_price(self):
            return self._price
    """
    

product1 = Product("iPhone 16", 80000)

print(product1.price)
product1.price = -90000
print(product1.price)

# product1.set_price(70000)
# print(product1.get_price())   => product1.price, product1.price = 70000
# print(product1.name, product1.price)