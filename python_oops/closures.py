#in simple terms -
#A closure is an inner function that remembers and has access to variables in the local scope in which it was created
#even after the outer function has finished executing


def outer_func():
    message = 'hi'  #free variable - not exactly defined within the inner function but we can still access it from inner_func

    def inner_func():
        print(message)  #message is a free variable

    return inner_func()



outer_func()



def outer_func():
    message = 'hi'  #free variable - not exactly defined within the inner function but we can still access it from inner_func

    def inner_func():
        print(message)  #message is a free variable

    return inner_func #*********** changed from above



my_new_func = outer_func() #now inner_func is assigned to my_new_func
print(my_new_func)
print(my_new_func.__name__ )


my_new_func()
