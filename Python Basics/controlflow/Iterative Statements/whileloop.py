#set object can be iterated using for loop only,since indexing is not possible.
'''
eids={101,102,103,104,101,102,103,104}
i=0
while i<=len(eids)-1:
    print(eids[i])
    i=i+1
 '''
    
ename="Nayana"
i=0
while i<=len(ename)-1:
    print(ename[i])
    i=i+1
    
for ch in ename:
    print(ch)
    
#print 1,2,3,5,6,7,8,9,10?
for i in range(1,11):
    if i==4:
        continue
    print(i)
    
i=0
while i<=9:
    i=i+1
    if i==4:
        continue
    print(i)