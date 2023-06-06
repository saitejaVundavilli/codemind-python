from math import gcd
a=int(input())
l=list(map(int,input().split()))
g=l[0]
for i in l:
    g=gcd(g,i)
print(g)
