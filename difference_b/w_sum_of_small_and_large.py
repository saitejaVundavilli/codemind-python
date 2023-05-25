a=list(input().split())
mi,ma=0,0
l1,l2=[],[]
for i in a:
    l1.append(min(i))
    l2.append(max(i))
for k in l1:
    mi+=ord(k)
for l in l2:
    ma+=ord(l)
print(abs(ma-mi))    