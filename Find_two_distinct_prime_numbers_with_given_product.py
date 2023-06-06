def prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
            break
    else:
        return True
        
a=int(input())
l=[]
for i in range(1,a+1):
    if prime(i)==True:
        l.append(i)
l1=[] 
c=0
for i in l:
    for j in l:
        if i*j==a:
            l1.append((i,j))
            c=1
            break
if c==1:
    print(*l1[0])
else:
    print(-1)