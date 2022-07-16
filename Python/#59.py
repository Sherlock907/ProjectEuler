"""
Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for
Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value,
taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text,
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random
bytes. The user would keep the encrypted message and the encryption key in different locations, and without both
"halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key.
If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message.
The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using p059_cipher.txt
(right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that
the plain text must contain common English words, decrypt the message and find the sum of the ASCII
values in the original text.
"""
import random
from string import ascii_lowercase as abc
from time import perf_counter as _p

s = _p()
encrypted = []

with open('#59', 'r') as f:
    for x in f.read().strip().split(","):
        encrypted.append(int(x))

#list with 1000 most common words
with open('#59-common', 'r') as f:
    common_words = f.read().split()

abc2, abc3 = ''.join(list(set(abc))), list(abc)
random.shuffle(abc3)
abc3 = ''.join(abc3)

#cipher to bytes
def ctb(c):
    return [int(ord(x)) for x in c]

def decode(cipher,encoded):
    cipher = ctb(cipher)
    tempcipher, tempencoded = cipher * (len(encoded)//3), []

    for code, char in zip(tempcipher,encoded):
        tempencoded.append(chr(code ^ char))


    tempencoded = ''.join(tempencoded).split()
    count = 0
    for x in tempencoded:
        if x in common_words:
            count += 1
    if count in mydict.keys():
        mydict[count].append(cipher)
    else:
        mydict[count] = cipher + [' '.join(tempencoded)]

mydict = {}
for a in abc:
    for b in abc2:
        for c in abc3:
            cipher = a+b+c
            decode(cipher,encrypted)


print(mydict.keys())
print(a:=max(mydict.items()), "\n")
temp = ""
for x in a[-1][-1].split():
    temp += x + " "
    if len(temp) >= 100:
        print(temp)
        temp = ""
print(sum([ord(x) for x in mydict[max(mydict.keys())][-1]]))
print(_p()-s)
