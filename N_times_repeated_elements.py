n=int(input())
l=list(map(int,input().split()))
k=int(input())
x=[]
a=[]
for i in l:
    if l.count(i)== k and i not in x:
        x.append(i)
if len(x)!=0:
    print(*x)
else:
    print("-1")