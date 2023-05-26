import math
def is_prime(n):
    if n==1:
        return False
    s=int(math.sqrt(n))
    for i in range(2,s+1):
        if n%i==0:
            return False
    return True
n1=int(input())
n2=int(input())
for i in range(1,n1+1):
    s=n1+n2+i
    if is_prime(s):
        print(i)
        break