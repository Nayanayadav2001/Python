fp=None
try:
    fp=open('xyz.txt','r')

except:
    fp=open('data.txt','r')


data=fp.read()
print(data)
print("Reading successfully")
fp.close()