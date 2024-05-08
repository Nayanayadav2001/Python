#read emp.csv file and print all employee names
import csv

fp=open('emp.csv','r')

emp_csv_obj=csv.reader(fp)
employees=list(emp_csv_obj)

for employee in employees:
    #print(employee[0])
    #print(employee[1])
    #print(employee[2])
    print("Id:",employee[0],"Name:",employee[1],"Gender:",employee[2])

fp.close()

