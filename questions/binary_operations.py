def return_bits(number):

    bits_arr = []
    while(number != 0):

        bits_arr.append(number %2)
        number = number // 2

        #return_bits(number // 2)

    print(bits_arr[-1::-1])


return_bits(10)


def return_number(binary):
    dec = 0
    decimal = 0
    i = 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2,i)
        binary = binary //10
        i = i + 1

    return decimal



#Swap two nibbles in a byte
#https://www.geeksforgeeks.org/swap-two-nibbles-byte/

#x can be int
def swapnibbles(x):

    return ( ((x & 0x0F) << 4) | ((x & 0xF0) >> 4) )

print(swapnibbles(5)) #80

#00000101 - 5
#01010000 - 80
