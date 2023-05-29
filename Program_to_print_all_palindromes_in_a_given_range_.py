def pal(x):
    v=str(x)
    b=v[::-1]
    if x==int(b):
        return x
    else:
        return 0
a=int(input())
b=int(input())
l=[]
for i in range(a,b+1):
    l.append(pal(i))
for j in l:
    if j==0:
        continue
    else:
        print(j,end=" ")