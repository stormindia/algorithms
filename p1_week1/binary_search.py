
def binary_search(array, k):

    low = 0
    high = len(array) - 1

    while(low <= high):
        mid = low + int((high -low)/2)
        if(k < array[mid]):         # one
            high = mid - 1          #   3
        elif(k > array[mid]):       #     way
            low = mid + 1           #         compare
        else:                       #       method
            return mid              # in binary_search

    return False


print(binary_search([1,2,4,5,6,7],7))

#max 1 + lgN compares
