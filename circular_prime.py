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
word=str(a)
al=word[::-1]
b=int(al)
call=is_prime(b)
if(count==2 and call==2):
    print("circular prime")
elif(count==2 and call!=2):
    print("prime but not a circular prime")
else:
    print("not prime")