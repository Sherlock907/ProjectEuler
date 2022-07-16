"""
An irrational decimal fraction is created by concatenating the positive integers:
0.123456789101112131415161718192021...
It can be seen that the 12th digit of the fractional part is 1.
If dn represents the nth digit of the fractional part, find the value of the following expression.
d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""
import math
import time

start = time.time()

thelongeststring = ""
for i in range(1000001):
    thelongeststring += str(i)
solution = int(thelongeststring[1])
for x in range(1,7):
    solution *= int(thelongeststring[10**x])
print(solution,time.time()-start)

# one-liner
start = time.time()
print(math.prod([int(''.join([str(i) for i in range(1000001)])[10**x]) for x in range(0,7)]),time.time()-start)

# two-liner
start = time.time()
a = ''.join([str(i) for i in range(1000001)])
print(int(a[1])*int(a[10])*int(a[100])*int(a[1000])*int(a[10000])*int(a[100000]),time.time()-start)
