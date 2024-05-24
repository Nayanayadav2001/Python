import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    username='root',
    password='root'
)
print(mydb)
print("connection successful")

cursor=mydb.cursor()
cursor.execute("CREATE DATABASE mydatabase")
print("created successfully")

