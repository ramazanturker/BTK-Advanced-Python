import time
import mysql.connector
from cachetools import cached, TTLCache

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "****",
    database = "shopdb"
)

@cached(cache=TTLCache(maxsize=32, ttl=60))
def getProducts():
    cursor = db.cursor()
    sql = "SELECT p.name, c.name FROM products p INNER JOIN categories c ON p.categoryid=c.id WHERE c.name='computer'"
    cursor.execute(sql)
    print("from sql")
    return cursor.fetchall()

s = time.time()
print(getProducts())
print("elapsed time:", time.time() - s)

s = time.time()
print(getProducts())
print("elapsed time:", time.time() - s)

s = time.time()
print(getProducts())
print("elapsed time:", time.time() - s)