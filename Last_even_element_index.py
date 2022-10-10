a=int(input())
list1=[]
list_a=list(map(int,input().split()))
for i in range(0,a):
    if(list_a[i]%2==0):
        list1.append(i)
leng=len(list1)
print(list1[leng-1])