import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ".****",
    database = "shopdb"
)

cursor = db.cursor()

sql = "INSERT INTO products (name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"

# value = ("iPhone 16",70000,"3.jpg","pretty phone")
# cursor.execute(sql, value)

values = [
    ("Samsung S23",80000,"7.jpg","pretty phone"),
    ("Samsung S24",90000,"8.jpg","nice phone"),
    ("Samsung S25",100000,"9.jpg","phone"),
]

cursor.executemany(sql, values)

try:
    db.commit()
    print(cursor.rowcount, "registration added")
    print(f"last registration id: {cursor.lastrowid}")
except mysql.connector.Error as err:
    print("error: ", err)
finally:
    cursor.close()
    db.close()
    print("connection closed")