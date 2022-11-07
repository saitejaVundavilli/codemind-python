a=int(input())
x=[]
s=0
l=list(map(int,input().split()))
a1,b1=map(int,input().split())
for i in range(0,a):
    if l[i]<a1 or l[i]>b1:
        x.append(l[i])
for i in x:
    s+=i
print(s)    
