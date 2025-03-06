import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "****",
    database = "shopdb"
)

cursor = db.cursor()

# sql = "SELECT name, categoryid FROM products"
# sql = "SELECT name FROM categories"
# sql = "SELECT products.name, categories.name FROM products INNER JOIN categories ON products.categoryid=categories.id"
# sql = "SELECT p.name, c.name FROM products p INNER JOIN categories c ON p.categoryid=c.id"
sql = "SELECT p.name, c.name FROM products p INNER JOIN categories c ON p.categoryid=c.id WHERE c.name='computer'"

cursor.execute(sql)

result = cursor.fetchall()

print(result)