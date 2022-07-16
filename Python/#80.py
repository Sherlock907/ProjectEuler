"""
It is well known that if the square root of a natural number is not an integer, then it is irrational.
The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
"""
import decimal

decimal.getcontext().prec = 105
res = 0
nsqrt = [x*x for x in range(1,11)]

for i in range(2,100):
    if i in nsqrt: continue
    res += sum([int(e) for e in str(decimal.Decimal(i).sqrt()).replace(".", "")[:100]])
print(res)
