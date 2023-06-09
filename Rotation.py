def rot(l,r):
    l1=l
    for i in range(r):
        l1.insert(0,l1[-1])
        l1.pop()
    return l1    
for i in range(int(input())):
    e,r=map(int,input().split())
    l=list(map(int,input().split()))
    e=rot(l,r)
    print(*e)