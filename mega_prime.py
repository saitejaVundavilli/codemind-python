def is_prime(b):
    prime=0
    for j in range(1,b+1):
        if(b%j==0):
            prime+=1
    return prime        
a=int(input())
count=0
for i in range(1,a+1):
    if(a%i==0):
        count+=1
while a:
    b=a%10
    a=a//10
    su=is_prime(b)
if(count==2 and su==2):
    print("Mega Prime")
else:
    print("Not Mega Prime")