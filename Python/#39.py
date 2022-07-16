"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p ≤ 1000, is the number of solutions maximised?
"""
import time
from collections import Counter

start = time.time()

clist = list()
solutioncount = 0
for a in range(1,1001):
    for b in range(1, 1001):
        c = (a**2 + b**2)**0.5
        if c == int(c) and a+b+c < 1001:
            clist.append(int(a+b+c))

r = Counter(clist)
print(r.most_common(1),time.time()-start)