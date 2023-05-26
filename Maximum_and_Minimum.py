n=int(input())
l=list(map(int,input().split()))
x=[]
for i in l:
    if l.count(i)==i and i not in x:
        x.append(i)
if len(x)!=0:
    print(min(x),max(x))
else:
    print("-1")