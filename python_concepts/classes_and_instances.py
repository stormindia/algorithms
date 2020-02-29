class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + "." + self.last + "@abc.com"

    def fullname(self):
        return "{} {}".format(self.first , self.last)


emp_1 = Employee('asd','qwe',100)
emp_2 = Employee('xyz','aaa',50)

print(emp_1.email)

print('{} {}'.format(emp_1.first, emp_1.last))
print(emp_1.fullname())
print(Employee.fullname(emp_1))
