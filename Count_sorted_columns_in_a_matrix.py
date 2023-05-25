r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
c1=0
for i in range(c):
    l=[]
    for j in range(r):
        l.append(mat[j][i])
    a=sorted(l)
    if a==l:
        c1+=1
    elif a[::-1]==l:
        c1+=1
print(c1)        