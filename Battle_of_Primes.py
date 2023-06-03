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
n1=int(input())
n2=int(input())
su=n1+n2
for i in range(1,su):
    if is_prime(su+i)==True:
        print(i)
        break