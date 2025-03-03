import csv

""" with open("/Users/turker/Desktop/BTK-Advanced-Python/05_csv_files/products2.csv", "w") as file:
    headers = ["Id","ProductName","Price","IsActive","Category","Rating"]
    csv_writer = csv.DictWriter(file, headers)
    csv_writer.writeheader()
    
    csv_writer.writerow({
         "Id": 1,
         "ProductName": "IPhone 14",
         "Price": 40000,
         "IsActive": True,
         "Category": "Phone",
         "Rating": 4.6
    })

    csv_writer.writerow({
         "Id": 2,
         "ProductName": "IPhone 15",
         "Price": 50000,
         "IsActive": True,
         "Category": "Phone",
         "Rating": 4.6
    })

    csv_writer.writerows([
        {
            "Id": 1,
            "ProductName": "IPhone 14",
            "Price": 40000,
            "IsActive": True,
            "Category": "Phone",
            "Rating": 4.6
        },
        {
            "Id": 2,
            "ProductName": "IPhone 15",
            "Price": 50000,
            "IsActive": True,
            "Category": "Phone",
            "Rating": 4.6
        },
        {
            "Id": 3,
            "ProductName": "IPhone 16",
            "Price": 60000,
            "IsActive": True,
            "Category": "Phone",
            "Rating": 4.6
        }
    ]) """

""" with open("/Users/turker/Desktop/BTK-Advanced-Python/05_csv_files/products2.csv", "a") as file:
    headers = ["Id","ProductName","Price","IsActive","Category","Rating"]
    csv_writer = csv.DictWriter(file, headers)
    
    csv_writer.writerow({
         "Id": 4,
         "ProductName": "IPhone 17",
         "Price": 70000,
         "IsActive": True,
         "Category": "Phone",
         "Rating": 4.6
    }) """

def price_tax(price):
    return float(price) * 1.20

with open("/Users/turker/Desktop/BTK-Advanced-Python/05_csv_files/products.csv") as file:
    csv_reader = csv.DictReader(file)
    products = list(csv_reader)

    with open("/Users/turker/Desktop/BTK-Advanced-Python/05_csv_files/products3.csv", "w") as file:
        headers = ["Id","ProductName","Price","IsActive","Category","Rating"]
        csv_writer = csv.DictWriter(file, headers)
        csv_writer.writeheader()

        for p in products:
            csv_writer.writerow({
                "Id": p["Id"],
                "ProductName": p["ProductName"],
                "Price": price_tax(p["Price"]),
                "IsActive": p["IsActive"],
                "Category": p["Category"],
                "Rating": p["Rating"]
            })