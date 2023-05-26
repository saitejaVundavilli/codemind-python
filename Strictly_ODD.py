n=int(input())
x=list(map(int,input().split()))
for i in range(n):
    if x[i]%2==0:
        if i%2!=0:
            print(False)
            break
else:
    print(True)