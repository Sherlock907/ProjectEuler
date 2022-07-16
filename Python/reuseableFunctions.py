import numpy
import math


def myNumpyPrimeSieve(n):
    isPrime = numpy.ones(n, dtype=bool)
    nmax = int(n ** 0.5 + 1)
    isPrime[0], isPrime[1] = False, False
    x, y = 2, 1
    while x <= nmax:
        if isPrime[x]:
            isPrime[x * 2::x] = False
        x += y
        y = 2
    return numpy.argwhere(isPrime)[:, 0]


def ispandigital(n):
    n =str(n)
    if len(n) > 9 or len(n) == 1:
        return False
    if (''.join(sorted(n))) == "123456789"[0:len(n)]:
        return True
    else:
        return False

def checkforpalindrome(n):
    n = str(n)
    if len(n) == 1:
        return True
    if n[0] == n[-1]:
        if len(n) == 2:
            return True
        return checkforpalindrome(n[1:len(n)-1])
    else:
        return False

def isPrime(n):
    nmax = int(n**0.5+1)
    counter = 3
    if n == 2: return True
    if n % 2 == 0: return False
    while counter <= nmax:
        if n % counter == 0: return False
        counter += 2
    return True

def getdivisors(n):
    return sorted(set(math.gcd(n,i) for i in range(1,n)))

def getfactors(n):
    nmax = int(n**0.5)+1
    factor_set = set()
    for i in range(2,nmax):
        if n % i == 0:
            factor_set.add(i)
            factor_set.add(int(n/i))
    factor_set.add(1)
    return sorted(factor_set)

if __name__ == "__main__":
    pass


