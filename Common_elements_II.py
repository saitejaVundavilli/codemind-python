a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l=[]
x=[]
for i in l1:
    if i not in l2 and i not in x:
        x.append(i)
for j in l2:
    if j not in l1 and j not in x:
        x.append(j)        
        
print(*x)        