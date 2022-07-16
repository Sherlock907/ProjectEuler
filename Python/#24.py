'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits
1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
from itertools import permutations

a = list(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8 ,9]))
print(''.join(str(e) for e in a[999999]))


#First Solution:
a = [0, 1, 2, 3, 4, 5, 6, 7, 8 , 9]
count = 0
for i in permutations(a):
    if count == 1000000-1:
        print(''.join(str(x) for x in i))
        break
    count += 1
