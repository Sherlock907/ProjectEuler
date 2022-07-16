from sympy.ntheory import sieve
from time import perf_counter as _p

s = _p()
res = 0
for x in sieve.totientrange(2,1_000_001):
    res += x
print(res,_p()-s)