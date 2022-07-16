"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
By converting each letter in a word to a number corresponding to its alphabetical position and adding these values
we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle
number then we shall call the word a triangle word.
Using words.txt (right click and 'Save Link/Target As...'),
a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""
from string import ascii_lowercase as abc
import time
start = time.time()

def revamp(n):
    n = str(n).lower()
    myreturn = list()
    for x in n:
       myreturn.append(abc.index(x)+1)
    return myreturn


trianglen = [(int(0.5*n*(n+1))) for n in range(1,100)]

# open and format data from file
f = open('#42','r')
words = f.read().replace('"',"").split(",")

count = 0
for x in words:
    if sum(revamp(x)) in trianglen:
        count += 1
f.close()
print(count, round((time.time()-start)*1000,2),"ms")