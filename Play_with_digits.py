a=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    for j in str(i):
        s+=int(j)
print(s)        
