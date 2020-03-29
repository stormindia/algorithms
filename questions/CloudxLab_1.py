#Problem 1 solution (Python 3)

# Given an array X and a number y, find the contiguous subarray of smallest length whose sum is greater than y. Note that array X contains only the positive numbers
#
# Example
#
# Test 1 - X = [9, 18, 42, 98], y = 21
#
# Output subarray can be either [42] or [98]
#
# Test 2 - X = [9, 18, 2, 4, 5], y = 21
#
# Output subarray of smallest length is  [9, 18]


X = [9, 18, 42, 98]
#X = [9, 18, 2, 4, 5]
y = 21


smallest_length = 9999999
sum = 0

output_subarray_list = []

curr_arr = []

for i in range(len(X)):
    #check if a single element has sum greater than y
    #if so, append that element as list in the output_subarray_list
    #also, make all the other elements of the output_subarray_list which have more than 1 element empty
    if(X[i] > y):
        smallest_length = 1
        output_subarray_list.append([[X[i]]])
        for j in range(len(output_subarray_list)):
            if(output_subarray_list[j] == []):
                pass
            else:
                if(len(output_subarray_list[j][0]) > 1):
                    output_subarray_list[j] = []

    #if on first element of the contiguous Output array
    elif(len(curr_arr) < 1):
        sum = X[i]
        curr_arr.append(X[i])

    #if a contiguous array is currently going on
    else:
        sum = sum + X[i]
        curr_arr.append(X[i])
        if(sum > y and len(curr_arr) < smallest_length):
            output_subarray_list.append([curr_arr])
            smallest_length = len(curr_arr)

            #make the curr_arr empty so that from next iteration new contiguous array can be formed
            curr_arr = []


#print(output_subarray_list)

for i in output_subarray_list:
    if(i == []):
        pass
    else:
        print(i[0])
