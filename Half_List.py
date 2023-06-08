a=int(input())
l=list(map(int,input().split()))
l1=l[:a//2]
l2=l[a//2:]
l2=l2[::-1]
c=l2+l1
print(*c)