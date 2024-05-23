import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    username="root",
    password="root",
    database="mydatabase"
)

cursor=mydb.cursor()

cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
print("created table successfully")