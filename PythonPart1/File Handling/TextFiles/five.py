# 'w'-mode writes data into specified file
# If file not exist, creates new file
# override happens
fp=open('emp.txt','w')

fp.write("Good night")
fp.close()