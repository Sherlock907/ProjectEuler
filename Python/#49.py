"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
(i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but
there is one other 4-digit increasing sequence.
What 12-digit number do you form by concatenating the three terms in this sequence?
"""
from reuseableFunctions import  myNumpyPrimeSieve
import time
start = time.time()

primes = myNumpyPrimeSieve(10_000)
for x in primes[primes > 1000]:
    for i in range(1000,10000-x*2):
        if (''.join(sorted((str(x)))) == ''.join(sorted((str(a:=x+i)))) == ''.join(sorted((str(b:=x+i*2))))
                and (a) in primes and (b) in primes):
            print(x,a,b)
print(round(time.time()-start,2), "s")
