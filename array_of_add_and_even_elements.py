a=int(input())
l=list(map(int,input().split()))
k=[]
l1=[]
for i in range(0,a):
    if(l[i]%2!=0):
        k.append(l[i])
    else:
        l1.append(l[i])
new=k+l1
for i in new:
    print(i,end=" ")