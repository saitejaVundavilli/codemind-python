n=int(input())
l=list(map(int,input().split()))
x=[]
for i in l:
    if l.count(i)==i and i not in x:
        x.append(i)
print(len(x))