a=input()
z,o=0,0
for i in a:
    if i=='z':
        z+=1
    else:
        o+=1
if o==z*2:
    print('Yes')
else:
    print('No')
        