def is_pal(n):
    s=str(n)
    return s==s[::-1]
def is_prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return True
    else:
        return False
a=int(input())
num=a
while num:
    num+=1
    if is_pal(num)==True and is_prime(num)==True:
        break
print(num)    