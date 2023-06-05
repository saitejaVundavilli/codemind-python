def is_prime(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        return True
    else:
        return False
i=int(input())
j=int(input())
for k in range(i,j):
    if is_prime(k)==True:
        print(k)