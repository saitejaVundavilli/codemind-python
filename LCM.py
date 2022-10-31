def ele(x):
    l1=[]
    for i in range(1,100):
        l1.append(x*i)
    return l1        
a,b=map(int,input().split())
lis=set(ele(a))
lis2=set(ele(b))
uni=lis&lis2
print(min(uni))

