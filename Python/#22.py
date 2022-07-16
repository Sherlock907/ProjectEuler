"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over
five-thousand first names, begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?
"""
from time import perf_counter as p
start = p()
f = open("#22", "r")
a, res = [], []

for i in f:
    a = i.replace('"', '').split(",")

a = sorted(a)


for x in range(len(a)):
    temp, tempres = [], 0
    for y in a[x]:
        temp.append(ord(y)-64)
    for j in temp:
        tempres += j
    res.append(tempres*(x+1))

print(sum(res),p()-start)