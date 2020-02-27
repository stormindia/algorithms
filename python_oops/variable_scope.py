'''
LEGB rule
Local, Enclosing, Global, Built-in
This is the scope order in which python searches the variable
'''


x = 'global_x'


def test_local(z):
    #z and x(below defined) are local
    x = 'Local_x'
    print(x)

#test('hello')
#print(x)

def test_global():
    global x
    x = 'Local_x'   #global x value will be changed
    print(x)

#test_global()
#print(x)


import builtins
#print(dir(builtins))

def test_built_in():
    m = min([1,2,3,4,5])    #min is builtin function
    print(m)


#test_built_in()


def test_enclosing():
    x = 'outer_x'   #enclosed variable

    def inner():
        #x = 'inner x'  #on commenting outer_x will be printed
        print(x)

    inner()
    print(x)

#test_enclosing()




def test_enclosing_non_local():
    x = 'outer_x'   #enclosed variable

    def inner():
        nonlocal x
        x = 'inner x'  #on commenting outer_x will be printed
        print(x)       #outer_x will also be changed

    inner()
    print(x)

test_enclosing_non_local()
