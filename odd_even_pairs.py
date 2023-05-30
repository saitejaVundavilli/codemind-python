n = int(input())
lst = list(map(int,input().split()))
e = [] # 2 4 6
o = [] #1 3 5 7 [3:4]
r=[] # 2 1 4 3 6 5 7
for i in lst:
    if i%2 == 0:
        e.append(i)
    else:
        o.append(i)
if len(o) >=len(e): # od--4 eve--3
    for i in range(len(e)):
        r.append(o[i])
        r.append(e[i])
    r=r+o[len(e):len(o)]
if len(o)<len(e):
    for i in range(len(o)):
        r.append(o[i])
        r.append(e[i])
    r=r+e[len(o):len(e)]
if len(lst)%2==0: #7
    print(*r)
else:
    r=r+[0] # 2 1 4 3 6 5 7
    print(*r)