# with open("/Users/turker/Desktop/BTK-Advanced-Python/05_csv_files/products.csv") as file:
#    print(file.read())

import csv

with open("/Users/turker/Desktop/BTK-Advanced-Python/05_csv_files/products.csv") as file:
    csv_reader = csv.reader(file)
    print(csv_reader)
    # listing = list(csv_reader)
    # print(listing[1])

    for i in csv_reader:
        if i[3] == "True":
            print(f"id: {i[0]}, product name: {i[1]}")