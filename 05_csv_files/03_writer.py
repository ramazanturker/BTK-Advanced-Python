import csv

# with open("05_csv_files/cars.csv", "w", newline='') as file:
#     csv_writer = csv.writer(file)
#     # csv_writer.writerow(["Brand","Modal"])
#     # csv_writer.writerow(["Toyota","Corolla"])
#     # csv_writer.writerow(["Mazda","CX-5"])
#     csv_writer.writerows([["Brand","Modal"],["Toyota","Corolla"],["Toyota","Chr"]])

# with open("05_csv_files/cars.csv", "a") as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(["Mazda","CX-5"])

# with open("05_csv_files/products.csv") as file:
#     csv_reader = csv.reader(file)
#     with open("05_csv_files/new_products.csv", "w", newline='') as f:
#         csv_writer = csv.writer(f)
#         for product in csv_reader:
#             csv_writer.writerow([p.upper() for p in product])

with open("05_csv_files/products.csv", "r+", newline='') as file:
    csv_reader = csv.reader(file)
    csv_writer = csv.writer(file)

    next(csv_reader)

    products = [[p[0],p[1],float(p[2])*1.2,p[3],p[4],p[5]] for p in csv_reader]

    file.seek(0)

    csv_writer.writerow(["Id","ProductName","Price","IsActive","Category","Rating"])
    csv_writer.writerows(products)