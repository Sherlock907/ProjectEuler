"""It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
"""
import time
start = time.perf_counter()
nmax = 100
ways = [1] + [0] * nmax
for div in range(1,nmax):
    for c in range(len(ways)-div):
        ways[c + div] += ways[c]

print(ways[-1], round((time.perf_counter()-start)*1000,2), "ms")
