def squaresum(n):
    sum=0
    while n:
        d=n%10
        n//=10
        sum+=d*d
    return sum
n=int(input())
x=squaresum(n)
while x>=10:
    x=squaresum(x)
if x==1:
    print("True")
else:
    print("False")