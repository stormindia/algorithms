import platform
print(platform.python_version())

nums = [1,2,3,4,5,6,7,8,9,10]


#list comprehension
my_list = [n for n in nums]
print(my_list)

#equivalent to
# for i in nums:
#     my_list.append(i)
# print(my_list)


my_list = [n *n for n in nums]

print(my_list)



my_list1 = [i for i in nums if i%2 ==0]

print(my_list1)
