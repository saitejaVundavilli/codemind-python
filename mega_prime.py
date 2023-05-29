def prime(a):
    c=0
    for i in range(1,a*2):
        if a%i==0:
            c+=1
    if c==2:
        return True
    else:
        return False
x=int(input())
y=prime(x)
v=str(x)
z=prime(int(v[0]))
n=prime(int(v[1]))
if y and z and n:
    print('Mega Prime')
else:
    print('Not Mega Prime')
