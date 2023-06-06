def is_prime(num): 
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    else:
        return True
a=int(input())
if is_prime(a)==False:
    ma=mi=a
    while True:
        ma+=1
        if is_prime(ma)==True:
            break
    while True:
        mi-=1
        if is_prime(mi)==True:
            break
    ld=abs(mi-a)
    hd=abs(ma-a)
    if ld<=hd:
        print(ld)
    else:
        print(hd)
else:
    print(0)