"""
The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28.
In fact, there are exactly four numbers below fifty that can be expressed in such a way:
28 = 22 + 23 + 24
33 = 32 + 23 + 24
49 = 52 + 23 + 24
47 = 22 + 33 + 24
How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
"""
from reuseableFunctions import myNumpyPrimeSieve
from time import perf_counter as pc

start = pc()
nmax = 50_000_000
primes = myNumpyPrimeSieve(int(nmax**0.5)+1)
squares = [i**2 for i in primes]
cubes = [i**3 for i in primes]
fourth = [i**4 for i in primes]
res = set()
mylist = list()

for a in squares:
    for b in cubes:
        if a + b > nmax: break
        for c in fourth:
            if a+b+c < nmax:
                res.add(a+b+c)
                mylist.append(a+b+c)
            else:
                break

print(len(res),len(mylist),pc()-start)


