import csv

with open("/Users/turker/Desktop/BTK-Advanced-Python/05_csv_files/online_foods.csv") as file:
    csv_reader = csv.reader(file)
    listing = list(csv_reader)
    print(len(listing) - 1)

with open("/Users/turker/Desktop/BTK-Advanced-Python/05_csv_files/online_foods.csv") as file:
    csv_reader = csv.DictReader(file)
    amount = len([user for user in csv_reader if user["Occupation"] == "Student"])
    print(amount)

with open("/Users/turker/Desktop/BTK-Advanced-Python/05_csv_files/online_foods.csv") as file:
    csv_reader = csv.DictReader(file)
    users = (user for user in csv_reader if int(user["Age"]) >= 20 and int(user["Age"]) <= 30)
    for i in users:
        print(i["latitude"], i["longitude"])