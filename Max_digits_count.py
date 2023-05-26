n=int(input())
l=list(map(str,input().split()))
a,a1=[],[]
for j in l:
    a.append(len(j))
for k in range(n):
    if a[k]==max(a):
        a1.append(l[k])
print(len(a1))