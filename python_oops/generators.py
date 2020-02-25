def square_num(num):
    for i in num:
        yield i*i   #generator


#my_nums = square_num([1,2,3,4,5])
#my_nums = [x*x for x in [1,2,3,4,5]] #list comprehension - not a generator

my_nums = (x*x for x in [1,2,3,4,5])  #generator

#print(list(my_nums))       #performance issues

for num in my_nums:
    print(num)
