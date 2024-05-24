import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    username="root",
    password="root",
    database="mydatabase"
)

cursor=mydb.cursor()

cursor.execute("insert into customers ()")
print("created table successfully")