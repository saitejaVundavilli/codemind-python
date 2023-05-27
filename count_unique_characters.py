a=list(map(str,input().lower().split()))
l,x=[],[]
for i in a:
    for j in i:
        if j not in l:
            l.append(j)
        else:
            x.append(j)
c=0            
for k in l:
    if k not in x:
        c+=1
print(c)        