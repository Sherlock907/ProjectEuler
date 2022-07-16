"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""

# formular: (2*n)! / (n!*n!)
n = 20
nMax = 1
nMax2 = 1
for i in range(1,41):
    if i < 21:
        nMax *= i
    nMax2 *= i
print(int((nMax2)/(nMax*nMax)))

