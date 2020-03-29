#URL - https://projecteuler.net/problem=4
import copy

def isPalindrome(n):
    number = n
    while(n > 0):
        a = n % 10
        rev = rev * 10 + a
        n = n / 10

    if(number == rev):
        return True
    else:
        return False


#max_palindrome = 0

palindromes = []
for x in range(100,999):
    for i in range(100,999):
        num = str(i*x).split()[0]
        if len(num) == 6:
            if num[0] == num[-1] and num[1] == num[-2] and num[2] == num[-3]:
                palindromes.append(i * x)
print(max(palindromes))



#Better solution
#https://www.xarg.org/puzzle/project-euler/problem-4/
