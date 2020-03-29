#URL - https://projecteuler.net/problem=5

num = 19*17*13*11 #*3*2*7*5*8*3

#finding LCM

power_arr=[[2,0],[3,0],[5,0],[7,0]]

arr = [20,18,16,14,12,15]


for i in arr:
    tmp = i
    count = 0
    for j in power_arr:
        while(tmp % j[0] == 0):
            tmp = tmp / j[0]
            count = count + 1
        if(count > j[1]):
            j[1] = count
        count = 0
        tmp = i

#print(power_arr)
for i in power_arr:
     num = num * pow(i[0],i[1])

print(num)
