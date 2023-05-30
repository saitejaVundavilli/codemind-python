import math
def is_prime(z):
   for i in range(2,int(math.sqrt(z))+1):
       if z%i==0:
           return False
   return True
a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    if is_prime(i) and i!=1:
        c+=1
print(c)