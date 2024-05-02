#whiledebugging
i=1
while i<=5:
    print(i)
    i=i+1
    
#while loop: if we want to execute a group of statements n number of times until the condition is false we use while loop.
#print 1-10 using for and while loop?
for i in range(1,11):
    print(i)
    
i=1
while i<=10:
    print(i)
    i=i+1
    
#iterate list oblect using for and while loop?
enames=["Rahul","Sonia","Priya","modi"]
for ename in enames:
    print(ename)
    
i=0
while i<=3:
    print(enames[i])
    i=i+1
    
#print 100-50 using while loop?
i=100
while i>=50:
    print(i)
    i=i-1
    
enames=["nayana","siri","shru","sunil"]
i=0
while i<=len(enames)-1:
    print(enames[i])
    i=i+1