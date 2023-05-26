a=int(input())
l=list(map(int,input().split()))
k=[]
l1=[]
for i in l:
    if i not in k:
        k.append(i)
for j in k:
    l1.append(j)
    l1.append(l.count(j))
print(*l1)    