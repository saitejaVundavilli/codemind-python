a=int(input())
for i in range(a):
    c,d=map(int,input().split())
    l=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    c1=sorted(l+l2)
    print(*c1)