#what is decorator?
def login_required(func):


    def inner(name,is_login):
        if is_login == False:
            print("Please Login")
        else:
            return func(name,is_login)
    return inner
        

@login_required
def home_page(name,is_login):
    print("home page")

@login_required
def order_page(name,is_login):
    print("order page")

@login_required
def product_page(name,is_login):
    print("product page")

@login_required
def profile_page(name,is_login):
    print("profile page")

home_page("siri",True)
order_page("siri",False)
product_page("siri",True)
profile_page("siri",False)