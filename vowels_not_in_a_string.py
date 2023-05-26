a=input()
l=[]
x=['a','e','i','o','u']
for i in a:
    if i not in l and i in x:
        l.append(i)
if len(l)==5:
   print(0)
else:
     for i in x:
        if i not in l:
            print(i,end=" ")