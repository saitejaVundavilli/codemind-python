from math import lcm
a=int(input())
l=list(map(int,input().split()))
print(lcm(*l))