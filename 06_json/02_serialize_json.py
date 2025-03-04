import json

product = {
    "id": 2,
    "title": "MacBook Pro",
    "price": 90000,
    "rating": "4.5",
    "category": "Computer",
    "colors": ["Red", "Blue"]
}

print(product)
print(product["title"])
print(type(product))

# result = json.dumps(product)

# print(result)
# print(result["title"])
# print(type(result))

with open("06_json/product.json", "w", encoding = "utf-8") as file:
    json.dump(product, file, ensure_ascii = False, indent = 2)