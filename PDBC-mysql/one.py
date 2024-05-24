#how to find the installed packages?
#pip list
import requests

resp=requests.get('https://jsonplaceholder.typicode.com/users')
user_list=resp.json

data=[]

for user in user_list:
    data.append((user['id'],user['name'],user['email'],user['address']['city'],user['phone']))


print(data)