def is_prime(j):
    count=0
    for i in range(1,j+1):
        if(j%i==0):
            count+=1
    if(count==2):
        return True
    else:
        return False
a=int(input())
list_a=[]
prime=0
for i in range(1,a+1):
    if(a%i==0):
        list_a.append(i)
for j in list_a:
    if(is_prime(j)==False):
        prime+=1
    else:
        pass
print(prime)    
        
    
    
        
