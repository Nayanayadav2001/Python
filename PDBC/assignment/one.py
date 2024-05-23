import requests

resp=requests.get('https://jsonplaceholder.typicode.com/users')

user_list=resp.json()
print(user_list)
print(type(user_list))

#print(help(requests))