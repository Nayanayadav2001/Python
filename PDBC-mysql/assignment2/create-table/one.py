import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydatabase"
)

cursor=mydb.cursor()
cursor.execute("create table employee(eid int,ename varchar(32),esal int)")
print("created table successfully")