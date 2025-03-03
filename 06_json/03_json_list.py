import json

data = [
    {
        "id": 1,
        "title": "MacBook Pro",
        "price": 80000
    },
    {
        "id": 2,
        "title": "MacBook Air",
        "price": 70000
    }
]

product = {
    "id": 3,
    "title": "Samsung S23",
    "price": 50000
}

with open("06_json/products.json") as file:
    products = json.load(file)

for p in products:
    if p["title"] == "Samsung S23":
        p["title"] = "Samsung S24"

products.remove(products[0])

# products.append(product)

with open("06_json/products.json", "w", encoding = "utf-8") as file:
    json.dump(products, file, ensure_ascii = False, indent = 2)