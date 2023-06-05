a=input()
c=0
s='aeiouAEIOU'
x=-1
for i in range(len(a)//2):
    if (a[i] in s and a[x]!=" " and a[x] not in s) or (a[i] not in s and  a[i]!=" " and a[x] in s):
        c+=1
        x-=1
    else:
        x-=1
print(c)    