def is_prime(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
        else:
            pass
    if c==2:
        return True
    else:
        return False
        
b=int(input())
st=str(b)
num=int(st[::-1])
if is_prime(b) and is_prime(num):
    print('circular prime')
elif is_prime(b)==True and is_prime(num)==False:
    print('prime but not a circular prime')
else:
    print('not prime')