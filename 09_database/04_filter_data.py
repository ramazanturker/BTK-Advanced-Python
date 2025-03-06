import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "****",
    database = "shopdb"
)

cursor = db.cursor()

# sql = "SELECT * FROM products WHERE id=1"
# cursor.execute(sql)
# result = cursor.fetchone()

# sql = "SELECT * FROM products WHERE id >= 1"
# sql = "SELECT * FROM products WHERE name = 'Samsung S25'"
# sql = "SELECT * FROM products WHERE name = 'Samsung S25' and price = 50000"
# sql = "SELECT * FROM products WHERE name = 'Samsung S25' or price = 50000"
# sql = "SELECT * FROM products WHERE name LIKE '%Samsung%'"
# sql = "SELECT * FROM products WHERE name LIKE 'Samsung%'"
# sql = "SELECT * FROM products WHERE name LIKE '%Samsung'"
# sql = "SELECT * FROM products WHERE name LIKE '%Samsung' or description LIKE '%pretty%'"
# cursor.execute(sql)
# result = cursor.fetchall()

def getProductById(id):
    sql = "SELECT * FROM products WHERE id = %s"
    params = (id,)
    cursor.execute(sql, params)
    result = cursor.fetchall()
    print(result)

getProductById(3)