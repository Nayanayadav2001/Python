def outer():
    print("outer function")

    def inner():
        print("inner function")


    print(type(inner))
    print(id(inner))

outer()