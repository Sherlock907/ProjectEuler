"""
A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers,
{a1, a2, ... , ak} is called a product-sum number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.

For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.

For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number.
The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.

k=2: 4 = 2 × 2 = 2 + 2
k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; note that 8
is only counted once in the sum.
In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is {4, 6, 8, 12, 15, 16}, the sum is 61.
What is the sum of all the minimal product-sum numbers for 2≤k≤12000?
"""
from math import prod
from time import perf_counter as _p

################################## First Working Solution ##################################
def firstWorkingSolution():
    _s = _p()
    nmax = 24_000
    res = [i*0 for i in range(0,12001)]
    k = 12_001
    kmax12res = [999999+1 for i in range(k)]

    kmax = k*2
    for a in range(2,k):
        for b in range(2, k):
            if a * b > kmax:break
            p = prod([a,b])
            s = sum([a,b])
            if p == s:
                if kmax12res[2] > p:
                    kmax12res[2] = p
            elif p - s + 2 < k:
                if kmax12res[p-s+2] > p:
                    kmax12res[p - s + 2] = p
            for c in range(2, k):
                if a * b * c > kmax: break
                p = prod([a, b,c])
                s = sum([a, b,c])
                if p == s:
                    if kmax12res[3] > p:
                        kmax12res[3] = p
                elif p - s + 3 < k:
                    if kmax12res[p - s + 3] > p:
                        kmax12res[p - s + 3] = p
                for d in range(2, k):
                    if a * b * c * d > kmax: break
                    p = prod([a, b, c,d])
                    s = sum([a, b, c,d])
                    if p == s:
                        if kmax12res[4] > p:
                            kmax12res[4] = p
                    elif p-s+4 < k:
                        if kmax12res[p - s + 4] > p:
                            kmax12res[p - s + 4] = p

                    for e in range(2, k):
                        if a * b * c * d * e> kmax: break
                        p = prod([a, b, c,d,e])
                        s = sum([a, b, c,d,e])
                        if p == s:
                            if kmax12res[5] > p:
                                kmax12res[5] = p
                        elif p - s + 5 < k:
                            if kmax12res[p - s + 5] > p:
                                kmax12res[p - s + 5] = p

                        for f in range(2, k):
                            if a * b * c * d * e * f > kmax: break
                            p = prod([a, b, c, d, e,f])
                            s = sum([a, b, c, d, e,f])
                            if p == s:
                                if kmax12res[6] > p:
                                    kmax12res[6] = p
                            elif p - s + 6 < k:
                                if kmax12res[p - s + 6] > p:
                                    kmax12res[p - s + 6] = p

                            for g in range(2, k):
                                if a * b * c * d * e * f * g > kmax: break
                                p = prod([a, b, c, d, e,f,g])
                                s = sum([a, b, c, d, e,f,g])
                                if p == s:
                                    if kmax12res[7] > p:
                                        kmax12res[7] = p
                                elif p - s + 7 < k:
                                    if kmax12res[p - s + 7] > p:
                                        kmax12res[p - s + 7] = p

                                for h in range(2, k):
                                    if a * b * c * d * e * f * g * h > kmax: break
                                    p = prod([a, b, c, d, e, f, g,h])
                                    s = sum([a, b, c, d, e, f, g,h])
                                    if p == s:
                                        if kmax12res[8] > p:
                                            kmax12res[8] = p
                                    elif p - s + 8 < k:
                                        if kmax12res[p - s + 8] > p:
                                            kmax12res[p - s + 8] = p

                                    for i in range(2, k):
                                        if a * b * c * d * e * f * g * h * i> kmax: break
                                        p = prod([a, b, c, d, e, f, g, h,i])
                                        s = sum([a, b, c, d, e, f, g, h,i])
                                        if p == s:
                                            if kmax12res[9] > p:
                                                kmax12res[9] = p
                                        elif p - s + 9 < k:
                                            if kmax12res[p - s + 9] > p:
                                                kmax12res[p - s + 9] = p

                                        for j in range(2, k):
                                            if a * b * c * d * e * f*g*h*i*j > kmax: break
                                            p = prod([a, b, c, d, e, f, g, h,i,j])
                                            s = sum([a, b, c, d, e, f, g, h,i,j])
                                            if p == s:
                                                if kmax12res[10] > p:
                                                    kmax12res[10] = p
                                            elif p - s + 10 < k:
                                                if kmax12res[p - s + 10] > p:
                                                    kmax12res[p - s + 10] = p

                                            for k2 in range(2, k):
                                                if a * b * c * d * e * f * g * h * i * j * k2> kmax: break
                                                p = prod([a, b, c, d, e, f, g, h, i, j,k2])
                                                s = sum([a, b, c, d, e, f, g, h, i, j,k2])
                                                if p == s:
                                                    if kmax12res[11] > p:
                                                        kmax12res[11] = p
                                                elif p - s + 11 < k:
                                                    if kmax12res[p - s + 11] > p:
                                                        kmax12res[p - s + 11] = p

                                                for l in range(2, k):
                                                    if a * b * c * d * e * f * g * h * i * j * l * k2 > kmax: break
                                                    p = prod([a, b, c, d, e, f, g, h, i, j, k2,l])
                                                    s = sum([a, b, c, d, e, f, g, h, i, j, k2,l])
                                                    if p == s:
                                                        if kmax12res[12] > p:
                                                            kmax12res[12] = p
                                                    elif p - s + 12 < k:
                                                        if kmax12res[p - s + 12] > p:
                                                            kmax12res[p - s + 12] = p

                                                    for m in range(2, k):
                                                        if a * b * c * d * e * f * g * h * i * j * k2 * l * m > kmax: break
                                                        p = prod([a, b, c, d, e, f, g, h, i, j, k2, l,m])
                                                        s = sum([a, b, c, d, e, f, g, h, i, j, k2, l,m])
                                                        if p == s:
                                                            if kmax12res[13] > p:
                                                                kmax12res[13] = p
                                                        elif p - s + 13 < k:
                                                            if kmax12res[p - s + 13] > p:
                                                                kmax12res[p - s + 13] = p

                                                        for n in range(2, k):
                                                            if a * b * c * d * e * f * g * h * i * j * k2 * l * m * n > kmax: break
                                                            p = prod([a, b, c, d, e, f, g, h, i, j, k2, l,m,n])
                                                            s = sum([a, b, c, d, e, f, g, h, i, j, k2, l,m,n])
                                                            if p == s:
                                                                if kmax12res[14] > p:
                                                                    kmax12res[14] = p
                                                            elif p - s + 14 < k:
                                                                if kmax12res[p - s + 14] > p:
                                                                    kmax12res[p - s + 14] = p

    print(sum(set(kmax12res[2:-1])))
    print(_p()-_s)
################################## First Working Solution END ##############################


######################## Recursive Solution inspired by the EulerForum ####################
def euler88():
    _s = _p()
    kmax = 12_001
    resliste = [999999 + 1 for i in range(kmax)]
    klimit = kmax * 2

    def myFun(p, s, d=0, start=2):
        k = p - s + d
        if k >= kmax: return
        if resliste[k] > p: resliste[k] = p
        for i in range(start, klimit // p + 1):
            myFun(p * i, s + i, d + 1, i)

    myFun(1, 0, 0, 2)
    print(resliste[2:13])
    print(sum(set(resliste[2:])))
    print(_p() - _s)


if __name__ == '__main__':
    euler88()
    firstWorkingSolution()


