a=int(input())
l=list(map(int,input().split()))
rev=l[::-1]
power=0
s=0
for i in rev:
    s+=(2**power)*i
    power+=1
print(s)    