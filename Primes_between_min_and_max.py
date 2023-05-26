def prime(n):
    if n==1 or n==0:
        return False
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True
n=int(input())
l=list(map(int,input().split()))
mn=l.index(min(l))
mx=l.index(max(l))
c=0
if mn<mx:
    for i in range(mn,mx+1):
        if prime(l[i]):
            c+=1
else:
    for i in range(mx,mn+1):
        if prime(l[i]):
            c+=1
print(c)