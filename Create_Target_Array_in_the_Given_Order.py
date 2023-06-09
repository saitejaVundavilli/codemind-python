a=int(input())
nums=list(map(int,input().split()))
b=int(input())
index=list(map(int,input().split()))
l=[]
for i in range(0,a):
    l.insert(index[i],nums[i])
print(*l)    
    
    

    