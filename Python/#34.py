"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""
from functools import lru_cache
import time
start = time.time()

@lru_cache
def sumof(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

result = []
for i in range(3,100000):
    tempresult,count = 0,0
    while count < len(str(i)):
        tempresult += sumof(int(str(i)[count]))
        count += 1
    if tempresult == i:
        result.append(i)

print(sum(result), result, time.time()-start)