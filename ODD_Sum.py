a=int(input())
sum1=0
l=list(map(int,input().strip().split()))
for i in range(0,a):
    if(l[i]%2!=0):
        sum1+=l[i]
print(sum1) 