a=int(input())
x=[]
l=list(map(int,input().split()))
a1,b1=map(int,input().split())
for i in range(0,a):
    if l[i]<a1 or l[i]>b1:
        x.append(l[i])
if(len(x)==0):
    print("-1")
else:
    print(max(x))