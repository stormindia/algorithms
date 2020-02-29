class A:

    def __init__(self):
        pass

    def a_method(self):
        print("A class method")



class B:

    def __init__(self):
        pass

    def a_method(self):
        print("B class method")



class C:

    def __init__(self):
        pass

    def __a_method(self):       #making a_method of C class private (add a dunder before method name)
        print("C class method")



class D(A,B,C):

    def __init__(self):
        #self.a_method()
        #B.a_method(self)
        D.__mro__[2].a_method(self)
        #D.__mro__[3].a_method(self)  #will throw error as a_method of C class is private(look below on how to access private method)
        #self.B.a_method()
        #super(B,self).a_method()

    def d_method(self):
        print("D class method")



obj1 = D()

#if you must call a private method -- name mangling
obj1._C__a_method()
