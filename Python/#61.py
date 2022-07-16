"""
Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) numbers and are generated by the following formulae:
Triangle 	  	P3,n=n(n+1)/2 	  	1, 3, 6, 10, 15, ...
Square 	  	P4,n=n2 	  	1, 4, 9, 16, 25, ...
Pentagonal 	  	P5,n=n(3n−1)/2 	  	1, 5, 12, 22, 35, ...
Hexagonal 	  	P6,n=n(2n−1) 	  	1, 6, 15, 28, 45, ...
Heptagonal 	  	P7,n=n(5n−3)/2 	  	1, 7, 18, 34, 55, ...
Octagonal 	  	P8,n=n(3n−2) 	  	1, 8, 21, 40, 65, ...

The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.

    The set is cyclic, in that the last two digits of each number is the first two digits of the next number (including the last number with the first).
    Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and pentagonal (P5,44=2882), is represented by a different number in the set.
    This is the only set of 4-digit numbers with this property.

Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.
"""
from time import perf_counter as p
from itertools import permutations as per

s = p()
tri, sq, pent, hexa, hept, octa = [],[],[],[],[],[]

for n in range(1,1000):
    tritemp = n*(n+1)/2
    sqtemp = n ** 2
    penttemp = n * (3 * n - 1) / 2
    hexatemp = n * (2 * n - 1)
    hepttemp = n * (5 * n - 3) / 2
    octatemp = n * (3 * n - 2)

    if len(str(int(tritemp))) == 4: tri.append(int(n*(n+1)/2))
    if len(str(int(sqtemp))) == 4: sq.append(int(n**2))
    if len(str(int(penttemp))) == 4: pent.append(int(n*(3*n-1)/2))
    if len(str(int(hexatemp))) == 4: hexa.append(int(n*(2*n-1) ))
    if len(str(int(hepttemp))) == 4: hept.append(int(n*(5*n-3)/2))
    if len(str(int(octatemp))) == 4: octa.append(int(n*(3*n-2)))

res = [tri, sq,pent,hexa,hept,octa]
#print(*res,sep="\n")

def theFuncTheWholeFuncAndNothingButTheFunc(liste):
    tri,sq,pent,hexa,hept,octa = liste[0],liste[1],liste[2],liste[3],liste[4],liste[5]
    myres = []
    for a in tri:
        for b in sq:
            if str(a)[2:4] != str(b)[0:2]:
                continue
            for c in pent:
                if str(b)[2:4] != str(c)[0:2]:
                    continue
                for d in hexa:
                    if str(c)[2:4] != str(d)[0:2]:
                        continue
                    for e in hept:
                        if str(d)[2:4] != str(e)[0:2]:
                            continue
                        for f in octa:
                            if str(e)[2:4] != str(f)[0:2]:
                                continue
                            if str(f)[2:4] == str(a)[0:2]:
                                myres.append([a,b,c,d,e,f])
                                print(myres,sum(myres[0]),p()-s)
                                exit()

permuted = per(res)
for l in permuted:
    theFuncTheWholeFuncAndNothingButTheFunc(l)