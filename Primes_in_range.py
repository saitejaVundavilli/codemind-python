import math
def is_prime(n):
    if n==1:
        return False
    s=int(math.sqrt(n))
    for i in range(2,s+1):
        if n%i==0:
            return False
    return True
m=int(input())
n=int(input())
c=0
for j in range(m,n+1):
    if is_prime(j):
        c+=1
print(c)