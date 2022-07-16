"""

It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?
"""
from reuseableFunctions import myNumpyPrimeSieve

primes = myNumpyPrimeSieve(100)
nmax = 1_000
ways = [1] + [0] * nmax

# dyamic programming
for prim in primes:
    for i in range(len(ways)-prim):
        ways[i + prim] += ways[i]
for count, v in enumerate(ways):
    if v > 5000:
        print(count,v)
        break
