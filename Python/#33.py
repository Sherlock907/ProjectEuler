"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting
to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits in the numerator and denominator.
If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""
#[[1, 5, 0.2], [19, 95, 0.2]]
#[[4, 8, 0.5], [49, 98, 0.5]]
#[[6, 8, 0.75], [48, 64, 0.75]]
#[[2, 5, 0.4], [26, 65, 0.4]]

from collections import Counter
import math
myl = []
stuff = []
myl2 = []
for i in range(10,100):
    for x in range(i, 100):
        if x == i:
            continue
        myl.append([i,x,i/x])
for i in range(1,10):
    for x in range(i,10):
        stuff.append([i,x,i/x])
for l1 in stuff:
    for i in range(len(myl)):
        if l1[2] == myl[i][2]:
            if (str(l1[0]) in str(myl[i][0]) or str(l1[0]) in str(myl[i][1])
                    or (str(l1[0]) in str(myl[i][0]) or str(l1[0]) in str(myl[i][1]))):
                if str(myl[i][0])[0] == str(myl[i][0])[1] or str(l1[0]) not in str(myl[i][0]):
                    continue
                uwu = "".join(str(l1[0])+str(l1[1])+str(myl[i][0])+str(myl[i][1]))
                if (len(set(uwu)) > 3 or ("0" in str(myl[i][0])) or ("0" in str(myl[i][1])) or
                        (str(l1[1]) in str(myl[i][0]) and str(l1[1]) in str(myl[i][1])) or
                            (str(l1[0]) in str(myl[i][0]) and str(l1[0]) in str(myl[i][1]))):
                    continue
                myl2.append([l1, myl[i]])

print(*myl2,sep="\n")
product1 = 1
product2 = 1
for i in range(0,len(myl2)):
    product1 *= myl2[i][1][1]
    product2 *= myl2[i][1][0]
print(product1, product2, "\nResult: ", product1//math.gcd(product1,product2))