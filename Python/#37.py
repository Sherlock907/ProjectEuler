"""
The number 3797 has an interesting property. Being prime itself,
it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7. Similarly we
can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
from reuseableFunctions import myNumpyPrimeSieve
import time
start = time.time()

def subprimes(n):
    n = str(n)
    # first and last number must be a single digit prime
    if int(n[0]) not in [2,3,5,7] or int(n[-1]) not in [2,3,5,7]:
        return False
    for i in range(1, len(n)):
        if int(n[:i]) in primes and int(n[i:]) in primes:
            continue
        else:
            return False
    return True

primes = myNumpyPrimeSieve(1000000)
sum = 0
for x in primes:
    if subprimes(x) and x not in [2,3,5,7]:
        sum += x
        print(x)
print(sum, time.time()-start)