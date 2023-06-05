a=input().lower().split()
s='aeiou'
c=0
for i in a:
    for j in range(0,len(i)//2):
        if i[j] in s and i[-(j+1)] not in s or i[j] not in s and i[-(j+1)] in s:
            c+=1
print(c)            
        