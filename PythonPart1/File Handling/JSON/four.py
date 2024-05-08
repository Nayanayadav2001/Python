import json
emp_json =''' {"id":101, "name":"Nayana","avail": true, "location": null}'''
#convert json to python dict type
print(type(emp_json))
emp_data=json.loads(emp_json)
print(emp_data)
print(type(emp_data))