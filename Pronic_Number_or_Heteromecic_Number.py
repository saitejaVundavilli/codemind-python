a=int(input())
fact=0
for i in range(1,a):
    if(i*(i+1)==a):
        fact=1
    else:
        pass
if(fact==1):
    print("YES")
else:
    print("NO")