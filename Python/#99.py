"""
Comparing two numbers written in index form like 211 and 37 is not difficult,
as any calculator would confirm that 211 = 2048 < 37 = 2187.
However, confirming that 632382518061 > 519432525806 would be much more difficult,
as both numbers contain over three million digits.
Using base_exp.txt (right click and 'Save Link/Target As...'),
a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.
NOTE: The first two lines in the file represent the numbers in the example given above.
"""
import time

# sadly takes 48 minutes to compute

start = time.time()
f = open("#99", "r")
res, line = [519432,525806], 0
count = 1

for x in f:
    print(line,"Count: ", count, res, time.time()-start)
    a = x.replace("\n","").split(",")
    if pow(int(a[0]),int(a[1])) > pow(int(res[0]),int(res[1])):
        res = a
        line = count
    count += 1

print(line, res, time.time()-start)
