a = """319
680
180
690
129
620
762
689
762
318
368
710
720
710
629
168
160
689
716
731
736
729
316
729
729
710
769
290
719
680
318
389
162
289
162
718
729
319
790
680
890
362
319
760
316
729
380
319
728
716
"""
a = a.split()

beforedict = {str(i):set() for i in range(0,10) if i not in [4,5]}
afterdict = {str(i):set() for i in range(0,10) if i not in [4,5]}

nested_dict = {
    'pos1': {str(i): i * 0 for i in range(0, 10)},
    'pos2': {str(i): i * 0 for i in range(0, 10)},
    'pos3': {str(i): i * 0 for i in range(0, 10)}
}

for x in a:
    nested_dict["pos1"][x[0]] += 1
    nested_dict["pos2"][x[1]] += 1
    nested_dict["pos3"][x[2]] += 1
    beforedict[x[-1]].update([x[1],x[0]])
    beforedict[x[1]].add(x[0])
    afterdict[x[0]].update([x[1], x[2]])
    afterdict[x[1]].add(x[2])


for x, y in afterdict.items():
    afterdict[x] = len(y)

print(''.join([y for y,x in reversed(sorted(afterdict.items(),key=lambda x:x[1]))]))
# print([[x,y] for x,y in list(afterdict.items())])



