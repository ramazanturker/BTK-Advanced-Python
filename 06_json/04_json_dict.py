import json

data = {
    "1": {
        "title": "MacBook Air",
        "price": 70000
    },
    "2": {
        "title": "Samsung S24",
        "price": 50000
    }
}

with open("06_json/products.json") as file:
    products = json.load(file)

print(products["1"])
print(products["2"])

""" products.update({
    "3": {
        "title": "MacBook Pro",
        "price": 80000
    }
}) """

products.update({
    "2": {
        "title": "Samsung S25",
        "price": 90000
    }
})

products.pop("3")

with open("06_json/products.json", "w", encoding = "utf-8") as file:
    json.dump(products, file, ensure_ascii = False, indent = 2)