import csv

with open("05_csv_files/products.csv") as file:
    csv_reader = csv.DictReader(file, delimiter=",")
    for i in csv_reader:
        if i["Category"] == "Phone" and float(i["Rating"]) >= 4.5:
            print(i["ProductName"], i["Price"])
