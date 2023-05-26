n=int(input())
l=list(map(int,input().split()))
x=[]
for i in l:
    if l.count(i)==i and i not in x:
        x.append(i)
if len(x)!=0:
    k=sum(x)/len(x)
    print('%.2f'%k)
else:
    print("-1")