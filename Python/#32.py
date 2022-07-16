"""

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""
#https://stackoverflow.com/questions/51538192/getting-all-combinations-of-a-string-and-its-substrings

import itertools
from time import perf_counter as _p
s = _p()
lis = [1,2,3,4,5,6,7,8,9]
a = itertools.permutations(lis)
count = 0
result = []
for i in a:
    x = str(i).replace(",","").replace(" ","").replace("(","").replace(")","")
    if int(x[0]) * int(x[1:3]) == int(x[3:9]):
        result.append([int(x[0]), int(x[1:3]), int(x[3:9])])
    if int(x[0:2]) * int(x[2:4]) == int(x[4:9]):
        result.append([int(x[0:2]) , int(x[2:4]) , int(x[4:9])])
    if int(x[0:3]) * int(x[3:4]) == int(x[4:9]):
        result.append([int(x[0:3]) , int(x[3:4]) , int(x[4:9])])
    if int(x[0:3]) * int(x[3:5]) == int(x[5:9]):
        result.append([int(x[0:3]), int(x[3:5]), int(x[5:9])])
    if int(x[0:3]) * int(x[3:6]) == int(x[6:9]):
        result.append([int(x[0:3]), int(x[3:6]), int(x[6:9])])
    if int(x[0:4]) * int(x[4:5]) == int(x[5:9]):
        result.append([int(x[0:4]) , int(x[4:5]) , int(x[5:9])])
    if int(x[0:5]) * int(x[5:6]) == int(x[5:9]):
        result.append([int(x[0:4]) , int(x[5:6]) , int(x[6:9])])

#only sum the products and every product once even when there are multiple ways to obtain it
resultsum = set()
for n in result:
    resultsum.add(n[2])
print(sum(resultsum),_p()-s)