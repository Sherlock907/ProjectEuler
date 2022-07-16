"""Euler discvered the remarkable quadratic formula:
It turns out that the formula will produce 40 primes for the consecutive integer values .
However, when is divisible by 41, and certainly when
is clearly divisible by 41.
The incredible formula
was discovered, which produces 80 primes for the consecutive values
. The product of the coefficients, −79 and 1601, is −126479.
Considering quadratics of the form:
, where and
where
is the modulus/absolute value of
e.g. and
Find the product of the coefficients,
and , for the quadratic expression that produces the maximum number of primes for consecutive values of , starting with .
n**2 + an + b
0-39
"""
from reuseableFunctions import myNumpyPrimeSieve
import time
start = time.time()
primes = myNumpyPrimeSieve(1000)
myl = [0,0,0,0]
highestcount = 0
#b should be a prime when n = 0
for b in primes:
    for a in range(-999,0):
        if (((41 ** 2) + (a * 41) + b)) not in primes:
            continue
        count = 0
        for n in range(1000):
            if ((n**2)+(a*n)+b) in primes:
                count += 1
                if count > highestcount:
                    highestcount = count
                    myl[0],myl[1] ,myl[2],myl[3]  = a*b,a,b,count
            else:
                break
# print(*myl,sep="\n")
print(myl[0])
print(time.time()-start)
