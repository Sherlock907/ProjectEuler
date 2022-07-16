def sumtoN(n):
    temp = 1
    for i in range(1,n+1):
        temp *= i
    return temp

def funcy(n,r):
    nsum = sumtoN(n)
    rsum = sumtoN(r)
    return nsum/(rsum*(sumtoN(n-r)))

n = 23
r = 10
print(funcy(n,r))
solution = 0
for i in range(1,101):
    for x in range(1,i):
        if funcy(i,x) > 1_000_000:
            solution += 1
print(solution)