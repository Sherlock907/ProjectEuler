"""
The number, 1_406_357_289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order,
 but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""
from itertools import permutations
import time
start = time.time()

def isPandigital(n):
    n = ''.join(sorted(str(int(n))))
    if n == "0123456789":
        return True
    return False

def haswierdprops(n):
    if (int(n[1:4])%2 == 0 and int(n[2:5])%3 == 0
        and int(n[3:6])%5 == 0 and int(n[4:7]) % 7 == 0
            and int(n[5:8])%11 == 0 and int(n[6:9])%13 == 0
                and int(n[7:10]) % 17 == 0):
        return True
    return False

# x is a permutation-object, the walrus operator makes it accessable in list-comprehension
print(sum([int(x2) for x in permutations("1023456789") if haswierdprops(x2:=''.join(x))]), round(time.time()-start,2),"s")




