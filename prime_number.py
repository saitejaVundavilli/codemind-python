a=int(input())
count=0
for i in range(2,a):
    if a%i==0:
        count=count+1
if count==0:
    print("prime")
else:
    print("not a prime")