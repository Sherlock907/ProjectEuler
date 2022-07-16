f = open("#67", "r")
mylist = [i.split() for i in f]
f.close()

#Int Conversion
for x in range(len(mylist)):
    mylist[x] = [int(i) for i in mylist[x]]

#Bottom to top
for i in reversed(range(len(mylist)-1)):
    for x in range(0,len(mylist[i])):
        mylist[i][x] += max(mylist[i+1][x+1],mylist[i+1][x])
print(max(mylist))