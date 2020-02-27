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

    def a_method(self):
        print("C class method")



class D(A,B):

    def __init__(self):
        #self.a_method()
        #B.a_method(self)
        D.__mro__[2].a_method(self)
        #self.B.a_method()
        #super(B,self).a_method()

    def d_method(self):
        print("D class method")



obj1 = D()
