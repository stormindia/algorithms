class Employee:

    raise_amt = 1.04  #class variable

    def __init__(self, first, last, pay):
        self.first = first  #instance variable --> unique to instance
        self.last = last #instance variable
        self.pay = pay #instance variable
        self.email = self.first + "." + self.last + "@abc.com"

    def fullname(self):
        return "{} {}".format(self.first , self.last)


    def __repr__(self):
        return "abcdef"

    def __str__(self):
        return "sdsdsd"

    def __add__(self,other):
        return self.pay + other.pay

    def __len__(self):
        return(len(self.fullname()))

emp1 = Employee('abc', 'def', 100)
emp2 = Employee('xyz', 'fgf', 300)

# print(str(emp1))
# print(repr(emp1))

print(emp1 + emp2)

print(len(emp1))
