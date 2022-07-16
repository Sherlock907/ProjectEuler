"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?
"""
from itertools import permutations
from reuseableFunctions import isPrime
from time import perf_counter as p

a, start, res = "123456789", p(), 0
for i in reversed(range(10)):
    for c,x in enumerate(permutations(a[0:i])):
        temp = int(''.join(x))
        if isPrime(temp):
            if temp > res:
                res = temp
    if res != 0:
        print(res,round((p()-start)*1000,1),"ms")
        break


