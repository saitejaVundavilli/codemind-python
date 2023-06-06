from itertools import permutations
m,n=map(int,input().split())
a=[]
for i in range(1,m+1):
    a.append(i)
l=list(permutations(a))
s=''
for i in l[n-1]:
    s+=str(i)
print(s)    