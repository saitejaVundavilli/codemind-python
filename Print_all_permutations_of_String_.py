from itertools import permutations
a=input()
l=permutations(a)
for i in l:
    print(''.join(i))