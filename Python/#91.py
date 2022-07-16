from sympy import Triangle, Point
from itertools  import combinations
from time import perf_counter as _P

#########################
## Hugely optimizeable ##
#########################

test = [0,0,0,2,2,2]

t = Triangle(Point(0, 3), Point(0, 0), Point(4, 0)).is_right()
t2 = Triangle(Point(0, 5), Point(0, 0), Point(11, 0)).is_right()
t3 = Triangle(Point(0, 9), Point(0, 0), Point(16, 0)).is_right()
# print(t,t2,t3)

s = _P()
myset, temppoints = set(), set()
nmax = 50
exceptioncounter = 0
for c in range(0, nmax):
    print(c, _P()-s)
    for d in range(0, nmax):
        for e in range(0, nmax):
            for f in range(0, nmax):
                if 0 not in [c,d,e,f]: continue
                try:
                    if Triangle(Point(0, 0), Point(c, d), Point(e, f)).is_right():
                        temp = [str(x) for x in [[0,0],[c,d],[e,f]]]
                        myset.add(''.join(sorted(temp)))
                except:
                    exceptioncounter += 1

print("\nResult:", len(myset),_P()-s)

# Result:  14234
# Runtime: 12495.42 s <- +3 Hours