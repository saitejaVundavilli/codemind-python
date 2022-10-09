def is_prime(j):
    count=0
    for i in range(1,j+1):
        if(j%i==0):
            count+=1
    if(count==2):
        return True
    else:
        return False
a=int(input())
b=int(input())
for j in range(a,b+1):
    if(is_prime(j)==True):
        print(j)
