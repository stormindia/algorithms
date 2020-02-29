# Lists -
# 1. Ordered
# 2. Hetrogeneous
# 3. Mutable (can be altered after creating)
# 4. List = [1,2,3,4]
#
# Tuples -
# 1. Ordered
# 2. Hetrogeneous
# 3. Immutable
# 4. tup = ('python', 'geeks')  or tup = 'python', 'geeks'
# 5. If an element of a tuple is Mutable in itself, then values inside that element can be changed
# 6. for example, if an element is a list inside a tuple, then we cah change the values of that list
#
# Dicitionary -
# 1. Unordered
# 2. Hetrogeneous key:value pairs
# 3. Values can be repeated but keys can't be repeated and keys should be immutable
# 4. Values for a key can be updated later on (mutable)
# 5. keys are case sensitive
# 6. Dict = dict({1: 'Geeks', 2: 'For', 3:'Geeks'}) or
#    Dict = dict([(1, 'Geeks'), (2, 'For')])
#
# Set -
# 1. Unordered
# 2. Mutable
# 3. Has duplicate elements
# 4. major advantage of using a set, as opposed to a list, is that it has a highly optimized method for
#    checking whether a specific element is contained in the set. This is based on a data structure known as a hash table.
# 5. Set = set(["a", "b", "c"])


############ TUPLES #####################
tup1 = (1,2,3,4,'a', [1,2,3])


print(tup1[-1])

tup1[-1][0] = 0 #==> works even though tuple is immutable

print(tup1[-1])

#tup1[1] = 22 ==> error

#############################################


Dict = dict({1: 'Geeks', 2: 'For', 3:'Geeks'})

print(Dict)
