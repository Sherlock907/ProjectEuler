"""

Let p(n) represent the number of different ways in which n coins can be separated into piles. For example,
five coins can be separated into piles in exactly seven different ways, so p(5)=7.
OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.
"""

# Runtime ~3-4 minutes

import time

start = time.perf_counter()
nmax = 56_000  # first guess 70_000
ways = [0*x for x in range(nmax)]
ways[0] = 1

for i in range(1, nmax):
    for w in range(len(ways) - i):
        ways[i + w] += ways[w] % 10_000_000

for count, x in enumerate(ways):
    if x % 1_000_000 == 0:
        print(count, time.perf_counter() - start)
        exit()
