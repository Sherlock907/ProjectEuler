"""
A number chain is created by continuously adding the square of the digits in a number to
form a new number until it has been seen before.
For example,
44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop.
What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""
import time
start = time.time()
count = 0
for i in range(1,10_000_000):
    temp = 0
    for c in str(i):
        temp += int(c)**2
    if temp == 89:
        count += 1

print(count, time.time()-start)
# 15309 32.27985095977783