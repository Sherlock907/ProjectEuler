"""
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.
37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49
It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is
that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.
If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed.
If this process is continued, what is the side length of the square spiral for which the ratio of primes
along both diagonals first falls below 10%?
"""
# 5 = 3; 9 = 5; 13 = 7;
from reuseableFunctions import myNumpyPrimeSieve, isPrime
from time import perf_counter as p_c
start = p_c()
primes = myNumpyPrimeSieve(100_000)
mylist = [1]
i = 1
pc = 0
while True:
    for x in range(0,4):
        if mylist[-1]+(2*i) > 100_000:
            if isPrime(mylist[-1]):
                pc += 1
        else:
            if mylist[-1]+(2*i) in primes:
                pc += 1
        mylist.append(mylist[-1]+(2*i))
    if pc/len(mylist)*100 < 10 and i not in [1,2]:
        print(int((len(mylist)+1)/2),(i+1)*2-1,"Time: ",round(p_c()-start,2), "s")
        exit()
    i += 1
