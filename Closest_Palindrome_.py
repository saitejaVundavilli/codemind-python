def is_pal(num):
    s=str(num)
    return s==s[::-1]
a=int(input())
small=larger=a
while True:
    small-=1
    if is_pal(small)==True:
        break
while True:
    larger+=1
    if is_pal(larger)==True:
        break
if abs(small-a) < abs(larger-a):
    print(small)
elif abs(small-a) == abs(larger-a):
    print(small,larger)
else:
    print(larger)