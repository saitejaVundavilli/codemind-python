x=int(input())
lst=list(map(int,input().split()))
l=len(lst)
c=0
for i in lst:
    if i==0 or i==1:
        c+=1
if c==l:
    print("True")
else:
    print("False")
