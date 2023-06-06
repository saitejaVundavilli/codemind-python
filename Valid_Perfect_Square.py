def sq(x):
    for i in range(1,x):
        if i**2==x:
            return True
            break
    else:
        return False
a=int(input())
for i in range(a):
    x=int(input())
    print(sq(x))