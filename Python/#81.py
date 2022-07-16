"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right
and down, is indicated in bold red and is equal to 2427.
Find the minimal path sum from the top left to the bottom right by only moving right and down in
matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix."""
from time import perf_counter as p

s = p()
# 80x80
newmatrix = []

with open("#81", "r") as file:
    for x in file:
        newmatrix.append(x.replace("\n", "").split(","))

#int Conversion
for x in range(len(newmatrix)):
    newmatrix[x] = [int(i) for i in newmatrix[x]]

for count,y in enumerate(newmatrix):
    for count2,x in enumerate(y):
        if count == 0 and count2 != 0:
            newmatrix[count][count2] += newmatrix[count][count2-1]
        if count2 == 0 and count != 0:
            newmatrix[count][count2] += newmatrix[count-1][count2]
        if count != 0 and count2 != 0:
            if newmatrix[count][count2]+newmatrix[count-1][count2] < newmatrix[count][count2]+newmatrix[count][count2-1]:
                newmatrix[count][count2]+=newmatrix[count-1][count2]
            else:
                newmatrix[count][count2]+=newmatrix[count][count2-1]

print(newmatrix[-1][-1],round((p()-s)*1000,2),"ms")
