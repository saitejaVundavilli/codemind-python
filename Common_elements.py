a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l=[]
x=[]
for i in l1:
    if i in l2 and i not in x:
        x.append(i)
print(*x)        