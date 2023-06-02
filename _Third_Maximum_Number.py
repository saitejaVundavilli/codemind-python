a=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    if i not in k:
        k.append(i)
j=sorted(k,reverse=True) 
if len(j)>2:
    print(j[2])
else:
    print(max(l))