"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values:
13, 23, 43, 53, 73, and 83, are all prime.
By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example
having seven primes among the ten generated numbers, yielding the family:
56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family,
is the smallest prime with this property.
Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit,
is part of an eight prime value family.
"""
import time
import numpy
from itertools import permutations
from reuseableFunctions import myNumpyPrimeSieve
from collections import Counter
primes1 = myNumpyPrimeSieve(1_000_000)
primes1 = primes1[primes1 > 100_000]
primes = numpy.array([i for i in primes1 if len(set(str(i)))<4])
# i guessed it would replace 3 digits and the results would be 6-digit longs

start = time.time()
for d in range(0,10):
    for b in range(0,10):
        for c in range(0, 10):
            temp , temp1 , temp2 , temp3 , temp4 , temp5 , temp6 , temp7, temp8 , temp9 , temp10, temp11 , temp12 ,temp13 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(),set()
            for a in range(0,10):
                if (mystr:=(int(str(a) + str(a)+ str(a) + str(b) + str(c) + str(d)))) in primes: temp.add(mystr)
                if (mystr1:=(int(str(a) + str(a) + str(b) + str(a) + str(c) + str(d)))) in primes: temp1.add(mystr1)
                if (mystr2:=(int(str(a) + str(a) + str(b) + str(c) + str(a) + str(d)))) in primes: temp2.add(mystr2)
                if (mystr3:=(int(str(a) + str(a) + str(b) + str(c) + str(d) + str(a)))) in primes: temp3.add(mystr3)
                if (mystr4:=(int(str(a) + str(b) + str(a) + str(a) + str(c) + str(d)))) in primes: temp4.add(mystr4)
                if (mystr5:=(int(str(a) + str(b) + str(c) + str(a) + str(a) + str(d)))) in primes: temp5.add(mystr5)
                if (mystr6:=(int(str(a) + str(b) + str(c) + str(d) + str(a) + str(a)))) in primes: temp6.add(mystr6)
                if (mystr7:=(int(str(b) + str(a) + str(c) + str(d) + str(a) + str(a)))) in primes: temp7.add(mystr7)
                if (mystr8:=(int(str(b) + str(c) + str(a) + str(d) + str(a) + str(a)))) in primes: temp8.add(mystr8)
                if (mystr9:=(int(str(b) + str(c) + str(d) + str(a) + str(a) + str(a)))) in primes: temp9.add(mystr9)
                if (mystr10:=(int(str(a) + str(b) + str(c) + str(a) + str(d) + str(a)))) in primes:temp10.add(mystr10)
                if (mystr11:=(int(str(a) + str(b) + str(a) + str(c) + str(a) + str(d)))) in primes: temp11.add(mystr11)
                if (mystr12:=(int(str(b) + str(a) + str(a) + str(c) + str(a) + str(d)))) in primes: temp12.add(mystr12)
                if (mystr13:=(int(str(b) + str(c) + str(a) + str(a) + str(a) + str(d)))) in primes: temp13.add(mystr13)
                if len(temp) == 8: print(sorted(temp),"\n",time.time()-start), exit()
                if len(temp1) == 8: print(sorted(temp1),"\n",time.time()-start), exit()
                if len(temp2) == 8: print(sorted(temp2),"\n",time.time()-start), exit()
                if len(temp3) == 8: print(sorted(temp3),"\n",time.time()-start), exit()
                if len(temp4) == 8: print(sorted(temp4),"\n",time.time()-start), exit()
                if len(temp5) == 8: print(sorted(temp5),"\n",time.time()-start), exit()
                if len(temp6) == 8: print(sorted(temp6),"\n",time.time()-start), exit()
                if len(temp7) == 8: print(sorted(temp7),"\n",time.time()-start), exit()
                if len(temp8) == 8: print(sorted(temp8),"\n",time.time()-start), exit()
                if len(temp9) == 8: print(sorted(temp9),"\n",time.time()-start), exit()
                if len(temp10) == 8: print(sorted(temp10),"\n",time.time()-start), exit()
                if len(temp11) == 8: print(sorted(temp11),"\n",time.time()-start), exit()
                if len(temp12) == 8: print(sorted(temp12),"\n",time.time()-start), exit()
                if len(temp13) == 8: print(sorted(temp13),"\n",time.time()-start), exit()
