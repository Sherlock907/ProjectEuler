"""
The first known prime found to exceed one million digits
was discovered in 1999, and is a Mersenne prime of the form 2**6972593−1;
it contains exactly 2,098,960 digits. Subsequently other Mersenne primes,
of the form 2p−1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains
2,357,207 digits: 28433×27830457+1.

Find the last ten digits of this prime number.
"""
from time import perf_counter as p
s = p()
#pow(x, y, z) is equal to x**y % z
result = 28433*pow(2, 7830457,10**10)+1
print(str(result)[-10:])
print(result%10**10,round((p()-s)*1000,3), "ms")

