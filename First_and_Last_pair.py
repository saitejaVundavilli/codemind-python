n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(len(l)//2):
        k.append(l[i])
        k.append(l[-i-1])
for i in range(len(l)):
    if l[i] not in k:
        k.append(l[i])
        k.append(0)
print(*k)