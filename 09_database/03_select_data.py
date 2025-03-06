import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ".****",
    database = "shopdb"
)

cursor = db.cursor()

# sql = "SELECT * FROM products"
sql = "SELECT id, name FROM products"


cursor.execute(sql)

# products = cursor.fetchall()
product = cursor.fetchone()

print(product)

# for product in products:
#     print(product[0], product[1])