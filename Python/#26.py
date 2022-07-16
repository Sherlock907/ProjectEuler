"""A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part."""


def reoccuringness(n):
    den = n
    remainder = 1 % den
    remainder_map = {}
    res = ""

    while remainder != 0 and remainder not in remainder_map:
        # print(remainder, remainder_map, remainder in remainder_map)
        remainder_map[remainder] = len(res)
        remainder *= 10
        res += str(remainder//den)
        remainder = remainder % den


    return res

res, res_len = 0,0
for i in range(2,1000):
    if (x:=len(reoccuringness(i))) > res_len:
        res = i
        res_len = x
print("Denominator: ", res," Lengths of reoccuring sequence: ", res_len)