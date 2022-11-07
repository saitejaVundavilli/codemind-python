a=int(input())
s,c=0,0
l=list(map(int,input().split()))
for i in l:
    s+=i
average=s//a
for i in l:
    if(i<=average):
        c+=1
print(c)        
