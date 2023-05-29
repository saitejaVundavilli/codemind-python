a1=list(map(str,input().lower().split()))
a=''.join(a1)
l=[]
for i in a:
    if a.count(i)==1:
        l.append(i)
        break
if len(l)!=0:
    print(*l)
else:
    print(-1)
    
