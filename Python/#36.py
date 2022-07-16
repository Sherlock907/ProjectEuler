"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def checkforpalindrome(n):
    if len(n) == 1:
        return True
    if n[0] == n[-1]:
        if len(n) == 2:
            return True
        return checkforpalindrome(n[1:len(n)-1])
    else:
        return False

sum = 0
for i in range(1000000):
    if checkforpalindrome(str(i)) and checkforpalindrome(str(bin(i))[2::]):
        print(str(bin(i))[2::], " ", i)
        sum += i
print(sum)