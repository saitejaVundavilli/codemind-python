a=list(input().split())
l=[]
for i in range(0,len(a)):
    if i%2==0:
        l.append(a[i][::-1])
    else:
        l.append(a[i])
print(*l)        
        