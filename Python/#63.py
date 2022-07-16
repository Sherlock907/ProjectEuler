"""
The 5-digit number, 16807=75, is also a fifth power.
Similarly, the 9-digit number, 134217728=89, is a ninth power.
How many n-digit positive integers exist which are also an nth power?
"""

count = 0
for x in range(1,1_000_000):
    for i in range(1,1000):
        if len(str(x**i)) == i:
            count += 1
        if len(str(x**i)) > i:
            break

print(count)
