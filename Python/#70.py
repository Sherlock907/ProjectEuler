"""
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of
positive numbers less than or equal to n which are relatively prime to n. For example,
as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.
Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.
Find the value of n, 1 < n < 10**7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
"""
import sympy
from time import perf_counter as _p
s = _p()

def checkifperm(x,y):
    x = str(x)
    y = str(y)
    if sorted(x) == sorted(y):
        return True
    return False


res = []
for i in range(2,10**7):
    if checkifperm((x:=sympy.totient(i)), i):
        res.append([i/x,i])
print(res)
print(min(res),_p()-s)
"""
Result : [1.0007090511248113, 8319823]
Runtime: 386.97s
"""