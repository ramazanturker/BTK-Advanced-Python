import json

class Product:
    def __init__(self, id, title, price):
        self.id = id
        self.title = title
        self.price = price

# serialize

""" product1 = Product(1, "Samsung S26", 70000)
product2 = Product(2, "Samsung S27", 80000)

# products = [product1.__dict__, product2.__dict__]
products = {
    product1.id : product1.__dict__,
    product2.id : product2.__dict__
}

with open("06_json/products.json", "w") as file:
    json.dump(products, file) """

# -----------------------------------------------------------------------

# deserialize

with open("06_json/products.json") as file:
    json_products = json.load(file)

print(type(json_products))

products = []

for key, value in json_products.items():
    products.append(Product(key, value["title"], value["price"]))

print(type(products))

for p in products:
    print(p.title)