import mysql.connector

try:
     dbcon=mysql.connector.connect(host='localhost',user='root',password='root')
     cursor=dbcon.cursor()
     sql_st='''
         insert into employee(eid,ename,esal) values(%s)
         '''
     data = [(102,'sonia',55000),(103,'priyanka',65000)]
     cursor.execute(sql_st)
     dbcon.commit()
     print('Data inserted successfully')

except:
     