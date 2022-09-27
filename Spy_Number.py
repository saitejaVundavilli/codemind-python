a=int(input())
sum=0
mul=1
while a:
    d=a%10
    sum=sum+d
    mul=mul*d
    a=a//10
if(mul==sum):
    print("Spy Number")
else:
    print("Not Spy Number")