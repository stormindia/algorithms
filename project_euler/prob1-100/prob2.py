#URL - https://projecteuler.net/problem=2

max = 4000000

curr_num = 2
prev_num = 1
sum = 2

while(curr_num < max):
    tmp = curr_num
    curr_num = curr_num + prev_num
    prev_num = tmp
    #print(curr_num)
    if(curr_num % 2 == 0):
        sum = sum+curr_num

print(sum)
