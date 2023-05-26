n=input()
x=n.lower()
lst=sorted(set(x))
for i in lst:
    if i==" ":
        continue
    else:
        print(i,end="")