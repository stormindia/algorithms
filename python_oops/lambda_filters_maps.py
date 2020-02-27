#lambda arguments: expression


def square(num):
    return num*num


#equivalent lambda function
abc = lambda x : print(x*x)

abc(5)

print(square(5))


#filter(function, sequence)
#returns an iterator that is already filtered.

array1 = [1,2,3,4,5,6,7,8,9,10]

new_arr = filter( lambda x: (x%2 == 0) , array1)

#filter returns an iterator
print(new_arr)

#to print all elements either use list() or next()
#print(list(new_arr))

print(next(new_arr))
print(next(new_arr))
print(next(new_arr))
print(next(new_arr))



def func(var):

    letters = ['a','b','d', 'e', 'f']

    if(var in letters):
        return True
    else:
        return False


sequence = ['a', 'b', 'c', 'i']

new_arr1 = filter(func, sequence)

print(list(new_arr1))


#map() function returns a map object(which is an iterator) of the results after applying the given function
#to each item of a given iterable (list, tuple etc.)

#map(fun, iter)

#Returns a list of the results after applying the given function
#to each item of a given iterable (list, tuple etc.)


array1 = [1,2,3,4,5,6]

ijk = map(lambda x: x*x, array1)

print(list(ijk))
