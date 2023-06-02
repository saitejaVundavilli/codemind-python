a1=int(input())
l=[0,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181]
for i in range(1,len(l)):
    if (l[i-1]<a1) and l[i]>a1:
        if abs(l[i-1]-a1) < abs(l[i]-a1):
            print(l[i-1])
        elif abs(l[i-1]-a1) == abs(l[i]-a1):
            print(l[i-1],l[i])
        else:
            print(l[i])
    