a=int(input())
for i in range(a):
    b=input()
    c=0
    l=[]
    for i in b:
        if i in 'ZXCVBNMASDFGHJKLQWERTYUIOPasdfghjklzxcvbnmqwertyuiop!@#$%^&*?':
            l.append(i)
            break
    if len(l)!=0:
        print(False)
    else:
        print('True')
        
        