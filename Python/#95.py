"""
The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of
28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.
Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220,
forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.
Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:
12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)
Since this chain returns to its starting point, it is called an amicable chain.
Find the smallest member of the longest amicable chain with no element exceeding one million."""
import math
import time
from functools import lru_cache

start = time.time()
#6 14 18
@lru_cache
def divsum(n):
    res = [1]
    nmax = int(n**0.5)+1
    for i in range(nmax,1,-1):
        if n % i == 0:
            res.append(i)
            res.append(n//i)
    return sum(res)

res = []
for i in range(1,15_000):
    if i % 100_000 == 0:
        print(i, time.time()-start)
    tempres = [i]
    a = divsum(i)
    while a not in tempres and a < 1_000_000 and a!=i:
        tempres.append(a)
        a = divsum(a)
    if a == i and len(tempres) != 1 and len(tempres) > len(res) and max(tempres)<1_000_000:
        res = tempres

print("Res: ", min(res),time.time()-start)