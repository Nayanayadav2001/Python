def login_required(func):

    def inner(name, is_login):
        
        if is_login == False:
            print("Login Required")
        else:
            return func(name,is_login)
    return inner
    
    
def home_page(name,is_login):
    print("Home Page")

def order_page(name,is_login):
    print("Order Page")
@login_required
def product_page(name,is_login):
    print("Product Page")
    
@login_required
def profile_page(name,is_login):
    print("Profile Page")
#sagar
home_page("sagar",True)
order_page("sagar",True)
product_page("sagar",False)
profile_page("sagar",True)