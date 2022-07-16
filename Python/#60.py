"""
The primes 3, 7, 109, and 673, are quite remarkable.
By taking any two primes and concatenating them in any order the result will always be prime.
For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792,
represents the lowest sum for a set of four primes with this property.
Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""
from reuseableFunctions import myNumpyPrimeSieve, isPrime
import time

start = time.time()
primes2 = myNumpyPrimeSieve(10_000)
primedict = {}

for a in primes2:
    primedict[a] = list()
    for b in primes2[primes2>a]:
        ab, ba = int(str(a)+str(b)), int(str(b)+str(a))
        if isPrime(ab) and isPrime(ba):
            primedict[a].append(b)

for a in primedict:
    for b in primedict[a]:
        for c in primedict[b]:
            if c not in primedict[a]: continue
            for d in primedict[c]:
                if d not in primedict[a]: continue
                if d not in primedict[b]: continue
                for e in primedict[d]:
                    if e not in primedict[a]: continue
                    if e not in primedict[b]: continue
                    if e not in primedict[c]: continue
                    print(a,b,c,d,e,"\nRes:",sum([a,b,c,d,e]))
                    print(round(time.time() - start,2),"s")
                    exit()



