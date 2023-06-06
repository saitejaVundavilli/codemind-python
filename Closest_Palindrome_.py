def is_pal(num):
    st=str(num)
    return st==st[::-1]
a=int(input())
low=high=a
while True:
    low-=1
    if is_pal(low)==True:
        break
while True:
    high+=1
    if is_pal(high)==True:
        break
if abs(low-a)<abs(high-a):
    print(low)
elif abs(low-a)==abs(high-a):
    print(low,high)
else:
    print(high)