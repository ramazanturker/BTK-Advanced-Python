import json

db = {
    "users": {
        "jessepinkman": {
            "firstname": "jesse",
            "lastname": "pinkman"
        },
        "janemargolis": {
            "firstname": "jane",
            "lastname": "margolis"
        }
    },
    "products": {
        "1": {
            "title": "MacBook Air",
            "price": 70000
        },
        "2": {
            "title": "Samsung S25",
            "price": 90000
        }
    }
}

with open("06_json/db.json") as file:
    data = json.load(file)

print(data["users"]["jessepinkman"])
print(data["products"]["2"]["price"])

data["products"].update({
    "3": {
        "title": "Samsung S26",
        "price": 100000
    }
})

data["users"].update({
    "jessepinkman": {
            "firstname": "jesse",
            "lastname": "pinkman",
            "age": 28
        },
})

with open("06_json/db.json", "w", encoding = "utf-8") as file:
    json.dump(data, file, ensure_ascii = False, indent = 2)