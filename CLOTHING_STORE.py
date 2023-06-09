a=int(input())
l=list(map(int,input().split()))
d={}
c=0
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in d.values():
        c+=i//2
print(c)        