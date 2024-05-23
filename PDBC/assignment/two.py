#import pymongo
import requests
from pymongo import MongoClient

resp=requests.get('https://jsonplaceholder.typicode.com/users')
user_list=resp.json()
#print(dir(pymongo))

client=MongoClient("mongodb://localhost:27017/")
print("Connection Succesful")
db=client['9am']
col=db['users']
col.insert_many(user_list)

print("Data inserted successfully")