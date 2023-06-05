a=input().split()
l=a[-1]
mi=min(l)
if mi.lower() in l:
    print(mi.lower())
else:
    print(mi)