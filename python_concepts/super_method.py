class A:

    def __init__(self):
        print("init of A")

    def a_method(self):
        print("A class method")



class B(A):

    def __init__(self):
        print('before super')
        super().a_method()
        #super().__init__()
        super(A).__init__()
        #super().__init__()
        print('after super')




obj1 = B()


#obj1.a_method()
