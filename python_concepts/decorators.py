#"A decorator is just a function that takes another function as an argument, adds some kind of functionality, and then returns another function."

# def decorator_funct(message):
#     def wrapper_func():
#         print(message)
#
#     return wrapper_func
#
#
#
# hi_func = decorator_funct('hi')
#
# bye_func = decorator_funct('bye')
#
# hi_func()
# bye_func()
#
#
# def decorator_funct(original_func):
#     def wrapper_func():
#         return original_func
#
#     return wrapper_func
#
# def display():
#     print('display func')
#
# #method 1
# decorated_display = decorator_funct(display)
# decorated_display()()
#
# #method 2
# decorated_display1 = decorator_funct(display())
# decorated_display1()


# print('\nuse of @ syntax below\n')
#
# #Use of @ syntax for decorator
# def decorator_funct(original_func):
#     def wrapper_func(*args, **kwargs):
#         print('wrraper function is being called before {}'.format(original_func.__name__))
#         return original_func(*args, **kwargs)
#
#     return wrapper_func
#
# @decorator_funct
# def display():
#     print('display func')
#
# display()                                   #both this line
# #displayyy = decorator_funct(display())      #and this line does the same thing
#
# @decorator_funct        #using the same decorator as above
# def display_info(name, age):
#     print('display_info arguments are {} {}'.format(name, age))
#
# display_info('asadad', 25)

#decorators in class
# class decorator_class:
#
#         def __init__(self,original_func):
#             self.original_func = original_func
#
#
#         def __call__(self,*args,**kwargs):
#             print('call method executed before{}'.format(self.original_func.__name__))
#             return self.original_func(*args,**kwargs)
#
# @decorator_class
# def display():
#     print('display func')
#
# display()                                   #both this line
# #displayyy = decorator_class(display())      #and this line does the same thing
#
# @decorator_class        #using the same decorator as above
# def display_info(name, age):
#     print('display_info arguments are {} {}'.format(name, age))
#
# display_info('asadad', 25)


from functools import wraps

def makebold(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        return "<b>" + fn(*args, **kwargs) + "</b>"
    return wrapped

def makeitalic(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        return "<i>" + fn(*args, **kwargs) + "</i>"
    return wrapped

@makebold
@makeitalic
def hello():
    return "hello world"

@makebold
@makeitalic
def log(s):
    return s

print(hello())        # returns "<b><i>hello world</i></b>"
print(hello.__name__) # with functools.wraps() this returns "hello"
print(log('hello'))   # returns "<b><i>hello</i></b>"
