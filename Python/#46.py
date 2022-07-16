"""
It was proposed by Christian Goldbach that every odd composite number can
be written as the sum of a prime and twice a square.
9 = 7 + 2×1**2
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.
What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
from reuseableFunctions import myNumpyPrimeSieve
import time

start = time.time()
nmax = 100_000
primes = myNumpyPrimeSieve(nmax)
mylist = [i for i in range(33, nmax, 2) if i not in primes]
for x in mylist:
    test = False
    for y in primes[primes < x]:
        if test == True:
            break
        for n in range(1,(x-y)):
            if x < y + 2*(n**2):
                break
            if (x == y + 2*(n**2)):
                test = True
                break
    if test == False:
        print("Composite Number: ", x)
        print(time.time() - start)
        break

