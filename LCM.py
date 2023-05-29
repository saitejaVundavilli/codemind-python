a,b=map(int,input().split())
x,y=[],[]
for i in range(1,a*2):
    x.append(i*a)
for j in range(1,b*2):
    y.append(j*b)
for a in x:
    if a in y:
        print(a)
        break
        
    