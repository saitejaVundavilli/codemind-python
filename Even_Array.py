a=int(input())
list1=list(map(int,input().split()))
leng=len(list1)
count=0
for i in range(0,leng):
    if(list1[i]%2!=0):
        count=1
        break
    else:
        pass
if(count==0):
    print("True")
else:
    print("False")
        