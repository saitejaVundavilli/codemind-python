a=int(input())
lis=list(map(int,input().split()))
set11=set(lis)
set1=list(set11)
count=0
leng=len(set1)
for i in range(0,leng):
    if(set1[i]%2==0):
        count+=1
print(count)   