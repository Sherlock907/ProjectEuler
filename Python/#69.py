import sympy
from time import perf_counter as _p
s = _p()
print(max([[i/sympy.totient(i), i] for i in range(2,1_000_001)]),_p()-s)
