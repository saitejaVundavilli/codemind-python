n=int(input())
a=0
b=1
l=[0,1]
for i in range(n-2):
    c=a+b
    a=b
    b=c
    l.append(c)
print(*l)    
    