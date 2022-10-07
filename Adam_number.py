a=int(input())
rev=0
sq1=a*a
while a:
    d=a%10
    rev=rev*10+d
    a=a//10
sq2=rev*rev
sqt2=str(sq2)
second=(sqt2[::-1])
print(sq1==int(second))