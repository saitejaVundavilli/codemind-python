n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    for j in range(i+1,n):
        if l[j]>=l[i]:
            c+=1
if c==0:
    print("yes")
else:
    print("no")