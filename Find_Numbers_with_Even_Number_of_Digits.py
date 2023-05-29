a=int(input())
l=list(map(str,input().split()))
c=0
for i in l:
    if len(i)%2==0:
        c+=1
print(c)        