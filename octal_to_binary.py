o=int(input())
d=0
i=0
while o:
    r=o%10
    d+=r*8**i
    i+=1
    o=o//10
print(bin(d).replace("0b",""))    