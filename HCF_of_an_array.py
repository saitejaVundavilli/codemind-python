from math import gcd
a=int(input())
l=list(map(int,input().split()))
c=l[0]
for i in l:
    c=gcd(i,c)
print(c)    