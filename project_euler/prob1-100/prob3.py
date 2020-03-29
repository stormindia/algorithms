#URL - https://projecteuler.net/problem=3
import math
num = 600851475143

for i in range(3,int(math.sqrt(num))+1,2):

    while(num % i == 0):
        curr_factor = i
        num = num // i

print(curr_factor)
