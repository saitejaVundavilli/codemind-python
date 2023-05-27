a=int(input())
l=list(map(int,input().split()))
x=0
d=0
for i in range(1,a-1):
    if l[i-1]<l[i] and l[i]>l[i+1]:
        x+=1
    else:
        d+=1
if d%2==0:
    print(-1)
else:
    print(x)
        