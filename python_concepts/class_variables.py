class Employee:

    raise_amt = 1.04  #class variable

    def __init__(self, first, last, pay):
        self.first = first  #instance variable --> unique to instance
        self.last = last #instance variable
        self.pay = pay #instance variable
        self.email = self.first + "." + self.last + "@abc.com"

    def fullname(self):
        return "{} {}".format(self.first , self.last)

    def apply_raise(self):
#        self.pay = self.pay*raise_amt  --> error
        self.pay = self.pay*self.raise_amt
                           # or Employee.raise_amt --> self is better to use (?)

emp_1 = Employee('asd','qwe',100)
emp_2 = Employee('xyz','aaa',50)

print(emp_1.email)

print('{} {}'.format(emp_1.first, emp_1.last))
print(emp_1.fullname())
print(Employee.fullname(emp_1))

print(emp_1.pay)

emp_1.apply_raise()

print(emp_1.pay)


emp_1.raise_amt = 1.05
emp_1.apply_raise()
print(emp_1.pay)
