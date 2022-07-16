"""
The cube, 41063625 (345**3), can be permuted to produce two other cubes:
56623104 (3843) and 66430125 (4053). In fact,
41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
Find the smallest cube for which exactly five permutations of its digits are cube.
"""
from time import perf_counter as pc
st = pc()
cubes = [str(i*i*i) for i in range(2,10_000)]
# cubes sorted
cs = [''.join(sorted(x)) for x in cubes]

for a in cubes:
    count_a = cs.count(''.join(sorted(a)))
    if count_a == 5:
        print(a, pc()-st)
        exit()
