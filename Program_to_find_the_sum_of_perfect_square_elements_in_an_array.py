a=int(input())
sum1=0
l=list(map(int,input().split()))
for i in l:
    for j in range(1,i+1):
        if i==j*j:
            sum1+=i
print(sum1)            
            