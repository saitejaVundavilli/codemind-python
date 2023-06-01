a=int(input())
l=list(map(int,input().split()))
s=''
for i in l:
    s+=str(i)
v=str(int(s)+1)
for i in v:
    print(i,end=" ")
