a=input().split()
l=''.join(a)
u,l1=[],[]
for i in l:
    if i in 'aeiou' and i not in l1:
        l1.append(i)
    elif i in 'AEIOU' and i not in u:
        u.append(i)
if len(l1)==5 or len(u)==5:
    print(True)
else:
    print(False)
