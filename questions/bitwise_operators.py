
a = 10  # 1010

b = 20 # 10100

print(a & b)    # 0

print(a or b)   # 10

print(b or a)   # 20

#NOT operator - returns one's compliment
#https://www.geeksforgeeks.org/1s-2s-complement-binary-number/

#**********
print(~a)   #Returns one’s compliement of the number. ==> also see binary_operations.py
#this will return -11
#explanation below ->
# binary of a(ie 10) = 00001010
# one's complement  = 11110101
#
# since the leading digit is 1, computer will store it as negative number
# how does computer stores negative number - as 2's complement of the number(adding 1 to one's complement)
# 1's complement of  11110101 -> 00001010
# add 1 to 1's complement -> 00001011  this is equal to 11
# but remeber it is a negative number and hence -11 will be printed


print(b ^ a)  #30  #Returns 1 if one of the bit is 1 and other is 0 else returns false.


#Shift operators
# Bitwise right shift: Shifts the bits of the number to the right and fills 0 on voids left as a result.
# Similar effect as of dividing the number with some power of two.

# a = 1010(10) >> 1 =  0101(5)
# b = 10100(20) >> 2 = 00101(5)
#
# shift by 1 place is equivalent to division by 2^1
# shift by 2 place is equivalent to division by 2^2


print(a >> 1)   #5
print(b >> 2)   #5


# Bitwise left shift: Shifts the bits of the number to the left and fills 0 on voids left as a result.
# Similar effect as of multiplying the number with some power of two.

# a = 00001010 << 1 = 00010100 (20)
# b = 00010100 << 2 = 01010000 (80) 20 * 2^2

print(a << 1)
print(b << 2)


print(256 << 1) #=> 512
