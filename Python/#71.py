from fractions import Fraction
from time import perf_counter as p

s = p()
res = 0
nmax = 1_000_000

for n in range(1,nmax):
    for d in range(int(n//(3/7))-1, int(n//(3/7))+2):
        if d > nmax: break
        if (x:=Fraction(n,d)) < Fraction(3,7) and x > res:
            res = x
print(res, p()-s)