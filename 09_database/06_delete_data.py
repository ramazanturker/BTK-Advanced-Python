import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "****",
    database = "shopdb"
)

cursor = db.cursor()

def deleteProductById(id):
    sql = "DELETE FROM products WHERE id = %s"
    # sql = "DELETE FROM products WHERE name LIKE '%s23%'"

    params = (id,)
    cursor.execute(sql, params)

    try:
        db.commit()
        print(f"{cursor.rowcount} quantity registrations deleted")
    except mysql.connector.Error as err:
        print(err)
    finally:
        db.close()
        cursor.close()

deleteProductById(3)