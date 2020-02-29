nums = [1,2,3]

#print(dir(nums))

#print(next(nums))      #error

#print(dir(iter))
i_nums = iter(nums)

print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
#print(next(i_nums)) #error here



#creating iterables

class myrange:

    def __init__(self,start,end):
        self.start = start
        self.end = end


    def __iter__(self):
       return self

    def __next__(self):

        if(self.start >= self.end):
            raise StopIteration
        curr = self.start
        self.start += 1
        return curr


nums = myrange(1,10)


print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
# print(next(nums))     #error
