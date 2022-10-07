a=int(input())
count=0
if a<0:
    count=1
else:
    pass
string=str(abs(a))
reverse=string[::-1]
if(count==1):
    print(-1*(int(reverse)))
else:
    print(int(reverse))