a=int(input())
sum1=0
mul=1
while a:
    d=a%10
    sum1+=d
    mul*=d
    a=a//10
print(mul-sum1)    