def fun(a):
    l=[]
    x=list(a)
    for i in range(0,len(a)):
        if x[i] not in '!@#$%^&*()_+':
            l.append(x[i])
            x[i]='*'
    p=sorted(l)
    j=0
    for i in range(len(x)):
        if x[i]=="*":
            x[i]=p[j]
            j+=1
    return ''.join(x) 
x=input().split()
for i in x:
    print(fun(i),end=" ")