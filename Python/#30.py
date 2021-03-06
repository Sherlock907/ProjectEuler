"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 84 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 14 is not a sum it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316.
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

def checkifsum(n):
    res = []
    n = str(n)
    for x in range(len(str(n))):
        if sum(res) > int(n):
            return False
        res.append(int(n[x])**5)
    if sum(res) == int(n):
        return True
    else:
        return False

myres = []
for i in range(2,(1000000)):
    if checkifsum(i):
        myres.append(i)

print(sum(myres))


