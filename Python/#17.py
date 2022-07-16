"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""
from string import ascii_lowercase
f = open("#17", "r")
numbers = ["zero"]
writtennumbers = ["zero"]
for s in f:
    a = s.strip().replace("\n", "").replace("0", "")
    b = a.find("–")
    if b == -1:
        continue
    numbers.append(len(a[b+2:].replace("-", "").replace(" ", "")))
    writtennumbers.append(a[b + 2:].replace("-", "").replace(" ", ""))
print(writtennumbers)
#print(writtennumbers)
#print(*writtennumbers, sep="\n")
count = 0


for i in range(1,1001):
    if i < 100:
        count += numbers[i]*10
    if i == 100:
        count += len("onehundred")
    if i > 100 and i <= 199:
        count += len("onehundredand")
    if i > 200 and i <= 299:
        count += len("twohundredand")
    if i > 300 and i <= 399:
        count += len("threehundredand")
    if i > 400 and i <= 499:
        count += len("tourhundredand")
    if i > 500 and i <= 599:
        count += len("fivehundredand")
    if i > 600 and i <= 699:
        count += len("sixhundredand")
    if i > 700 and i <= 799:
        count += len("sevenhundredand")
    if i > 800 and i <= 899:
        count += len("eighthundredand")
    if i > 900 and i <= 999:
        count += len("ninehundredand")
    if i == 1000:
        count += len("onethousand")
count += len("twohundred") + len("threehundred") + len("fourhundred") + len("fivehundred") + len("sixhundred") + len("sevenhundred") + len("eighthundred") + len("ninehundred")



print(count)

