a=int(input())
original=a
square=a*a
sum1=0
while square:
    d=square%10
    sum1=sum1+d
    square=square//10
if(sum1==original):
    print("Neon Number")
else:
    print("Not Neon Number")
    