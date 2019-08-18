#find three numbers whose sum is equal to given sum
#sort the array - time - N^2 - insertion sort
#find the triplet - N^2lgN

def three_sum(s):
    s = sorted(s) # O(nlogn)
    output = set()
    for k in range(len(s)):
        target = -s[k] #can replace with other number as well to genralise
        i,j = k+1, len(s)-1
        while i < j:
            sum_two = s[i] + s[j]
            if sum_two < target:
                i += 1
            elif sum_two > target:
                j -= 1
            else:
                output.add((s[k],s[i],s[j]))
                i += 1
                j -= 1
    return output

print(three_sum([-1, 0, 1, 2, -1, -4]))
