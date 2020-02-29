class Employee:

    raise_amt = 1.04  #class variable

    def __init__(self, first, last, pay):
        self.first = first  #instance variable --> unique to instance
        self.last = last #instance variable
        self.pay = pay #instance variable
        self.email = self.first + "." + self.last + "@abc.com"

    def fullname(self):  #regular method - takes self as first argument(or automatically takes instance as first argument)
        return "{} {}".format(self.first , self.last)

    def apply_raise(self):
        #self.pay = self.pay*raise_amt  --> error
        self.pay = self.pay*self.raise_amt
                           # or Employee.raise_amt --> self is better to use (?)


class developers(Employee):

    raise_amt = 1.05

    def __init__(self, first, last , pay, prog_lang):
        super().__init__(first, last, pay)
        #Employee(self, first, last, pay)

        self.prog_lang = prog_lang

class testers(Employee):

    raise_amt = 1.03


class managers(Employee):

    def __init__(self, first, last , pay, employees=None):
        super().__init__(first, last, pay)

        if employees is None :
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        self.employees.append(emp)

    def remove_emp(self, emp):
        self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(emp.fullname())



emp_1 = Employee('asd','qwe',100)
emp_2 = Employee('xyz','aaa',50)


dev_1 = developers('zxc' , 'bnm' , 500, 'java')
print(dev_1.raise_amt)
print(dev_1.fullname())
print(dev_1.prog_lang)
testers_1 = testers('ert', 'tyu' , 400)
print(testers_1.raise_amt)

#print(help(developers))

mgr_1 = managers('harshit', 'bajpai' , 50000, [emp_1, dev_1])

mgr_1.print_emps()

mgr_1.add_emp(emp_2)
mgr_1.print_emps()

mgr_1.remove_emp(emp_1)
mgr_1.print_emps()
