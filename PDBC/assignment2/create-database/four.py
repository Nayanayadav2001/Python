import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    username='root',
    password='root',
    database='mydatabase'
)
print("created database successfully")