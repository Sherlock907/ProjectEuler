"""
The first two consecutive numbers to have two distinct prime factors are:
14 = 2 × 7
15 = 3 × 5
The first three consecutive numbers to have three distinct prime factors are:
644 = 2**2 × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.
Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""
from reuseableFunctions import myNumpyPrimeSieve
import time,math

primes = myNumpyPrimeSieve(1000)
start = time.time()

def primefactors(n):
	results = set()
	prime = primes[primes < n]
	for i in range(len(prime)):
		if int(math.gcd(n,prime[i])) != 1:
			n = int(n/prime[i])
			results.add(prime[i])
	return results


for i in range(10_000, 250_000):
	if len(a:=primefactors(i)) >= 4:
		if len(b:=primefactors(i+1)) >= 4:
			if len(c:=primefactors(i+2)) >= 4:
				if len(d:=(primefactors(i+3))) >= 4:
					print(i,i+1,i+2,i+3, a,b,c,d)
					break

print(time.time()-start)