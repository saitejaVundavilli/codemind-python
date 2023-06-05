a=input().lower().split()
l1=[]
for i in a:
    c=0
    for j in i:
        if j in 'aeiou':
            c+=1
    l1.append(c)
x=0
l2=max(l1)
for i in l1:
    if i==l2:
        x+=1
print(x)       