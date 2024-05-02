def smart_div(func):

    def inner(a,b):
        if b==0:
            print("cant divide by zero")
        else:
            return func(a,b)
        
    return inner

@smart_div
def cal(a,b):
    print(a/b)


cal(10,1)
cal(10,0)
cal(10,2)