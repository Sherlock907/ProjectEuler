"""

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
from reuseableFunctions import myNumpyPrimeSieve
import time
start = time.time()

primes = myNumpyPrimeSieve(1_000_000)
results = []
for i in primes:
    myl = []
    myl.append(str(i)[1::] + str(i)[0])
    isEven = False
    if len(str(i)) > 1:
        for x in str(i):
            if int(x) % 2 == 0:
                isEven = True
    if isEven:
        continue
    for s in range(len(str(i))):
        if len(str(i)) == 1:
            continue
        elif (str(myl[-1])[1::] + str(myl[-1])[0]) in myl:
            break
        myl.append(str(myl[-1])[1::] + str(myl[-1])[0])
    for x in myl:
        if int(x) in primes:
            if x == myl[-1]:
                results.append(i)
        else:
            break
print(len(results))
# print(results)
print(time.time()-start)