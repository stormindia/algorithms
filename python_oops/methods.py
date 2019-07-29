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
#        self.pay = self.pay*raise_amt  --> error
        self.pay = self.pay*self.raise_amt
                           # or Employee.raise_amt --> self is better to use (?)

    @classmethod
    def set_raise_amt(cls, amount): #automatically takes class as first argument
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first , last , pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6 :
            return "weekend"
        else:
            return "weekday"


emp_1 = Employee('asd','qwe',100)
emp_2 = Employee('xyz','aaa',50)

print(emp_1.email)

print('{} {}'.format(emp_1.first, emp_1.last))
print(emp_1.fullname())
print(Employee.fullname(emp_1))

# print(emp_1.pay)
#
# emp_1.apply_raise()
#
# print(emp_1.pay)
#
#
# emp_1.raise_amt = 1.05
# emp_1.apply_raise()
# print(emp_1.pay)

print(emp_1.raise_amt)
print(emp_2.raise_amt)

Employee.set_raise_amt(10)  #automatically takes class as first argument

print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = 'abc-def-1000'
emp_str_2 = 'ghj-klm-2000'

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)

print(new_emp_1.email)


import datetime
my_date = datetime.date(2019 , 7 , 28)
print(Employee.is_workday(my_date))
