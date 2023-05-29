def fun(x):
    m=0
    c=0
    for i in range(1,x*2):
        if x%i==0:
            c+=1
    if c==2:
        m+=1
    return m    
        
a=int(input())
l=[]
for i in range(1,a+1):
    if a%i==0:
        l.append(i)
v=[]        
for i in l:
    v.append(fun(i))
print(len(l)-sum(v))    