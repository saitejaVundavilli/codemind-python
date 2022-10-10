a=int(input())
sum1=0
list_a=list(map(int,input().split()))
for i in range(0,a,2):
    sum1+=list_a[i]
print(sum1)    