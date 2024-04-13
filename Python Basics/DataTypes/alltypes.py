price=389
print(type(price))

rating=4.5
print(type(rating))

product_name='Mens shirt'
print(type(product_name))

c=10+20j
print(type(c))

avail=True
print(type(avail))

size=[38,40,42,44]
print(type(size))

t=(38,40,42,44)
print(type(t))

ids={101,102,103,104}
print(type(ids))

emp={'id':101,'name':'Nayana'}
print(type(emp))

#group of elements should be btw 0-256 for bytes
b=bytes([200,10,230,129])
print(type(b))

ba=bytearray([20,255,149,49])
print(type(ba))

fs=frozenset({101,102,103,104})
print(type(fs))

r=range(100)
print(type(r))

a=None
print(type(a))

def add():
    pass
print(type(add()))