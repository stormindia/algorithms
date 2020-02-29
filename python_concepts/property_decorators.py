#GETTERS - TO access a class like an attribute

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        #self.email = self.first + "." + self.last + "@abc.com"

    #getter
    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first , self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    ## also see deleters


emp_1 = Employee('asd','qwe',100)
emp_2 = Employee('xyz','aaa',50)

print(emp_1.first)
print(emp_1.email)  #email is a method now but we can still use it as an attribute

emp_1.fullname = 'asdasd asdds'
print(emp_1.fullname)
print(emp_1.email)
