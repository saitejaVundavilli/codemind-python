def fact(n):
    c=1
    for i in range(1,n+1):
        c=c*i
    return c
a=int(input())
z=a
k=0
while a:
    d=a%10
    a=a//10
    k+=fact(d)
if k==z:
    print('The number '+str(z)+' is a strong number')
else:
    print('The number '+str(z)+' is not a strong number')