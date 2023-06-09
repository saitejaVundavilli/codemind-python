c=0
for i in range(int(input())):
    s=input()
    if (s[1]=="+" and(s[0]=="+" or s[2]=="+")):
        c+=1
    elif (s[1]=="-" and(s[0]=="-" or s[2]=="-")):
        c-=1
print(c)