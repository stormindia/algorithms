import copy

arr1 = [1,2,3,4]

#arr2 = copy.copy(arr1)         #deep copying (but according to gfg this is shallow ?????)
arr2 = arr1             #shallow copy

print(arr1)
print(arr2)


print('change element')

arr1[0] = 0

print(arr1)
print(arr2)



https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/

1a
arr = [0]*N


Method 1b
arr = [0 for i in range(N)]


Method 2a
arr = [[0]*cols]*rows


Method 2b
arr = [[0 for i in range(cols)] for j in range(rows)]
