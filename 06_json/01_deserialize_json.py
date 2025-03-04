import json

# with open("06_json/product.json") as file:
#     data = json.load(file)

# json string
data = """
    {
        "id": 1,
        "title": "MacBook Pro",
        "price": 90000,
        "rating": "4.5",
        "category": "Computer",
        "colors": ["Red", "Blue"]
    }
"""

data = json.loads(data)

print(data)
print(type(data))
print(data["title"])
print(data["price"])
print(data["colors"])