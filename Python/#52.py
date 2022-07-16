"""
It can be seen that the number, 125874, and its double, 251748,
contain exactly the same digits, but in a different order.
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""
import time
start = time.time()
def numbercheck(n):
    mylist = []
    for i in range(2,7):
        mylist.append(''.join(sorted(str(n*i))))
    if mylist[0] == mylist[1] == mylist[2] == mylist[3] == mylist[4] == ''.join(sorted(str(n))):
        return True
    return False

count = 1
while numbercheck(count) == False:
    count += 1
print(count)
print(round((time.time()-start)*1000,1),"ms\n")

# one-liner
start = time.time()
print(min([i for i in range(1,175_000) if ''.join(sorted(str(1*i))) == ''.join(sorted(str(2*i))) == ''.join(sorted(str(3*i))) == ''.join(sorted(str(4*i))) == ''.join(sorted(str(5*i))) == ''.join(sorted(str(6*i)))]))
print(round((time.time()-start)*1000,1),"ms")