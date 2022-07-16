'''
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.
The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms,
and is equal to 953.
Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''
from time import perf_counter  as p
from reuseableFunctions import myNumpyPrimeSieve


def letsgo():
    b = myNumpyPrimeSieve(1000000)

    myList,res,currentHighest = b.tolist(),0,0
    for i in range(1,len(b)):
        if sum(b[i:i+currentHighest]) > 1000000:
            break
        for k in range(2,len(b)-1):
            thesum = sum(myList[i:k])
            if thesum > 1000000 or i + k >= len(b):
                break
            if currentHighest < k-i and thesum > res and thesum in b:
                currentHighest = k-i
                res = thesum

    print("Result: ", res)

if __name__ == "__main__":
    start = p()
    letsgo()
    print(round((p()-start)*1000,1), "ms")