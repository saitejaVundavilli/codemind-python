a=int(input())
word=str(a)
count=0
le=len(word)
for i in range(0,le):
    for j in range(0,le):
        if(word[i]==word[j]):
            count+=1
        else:
            pass
if(count==le):
    print("Unique Number")
else:
    print("Not Unique Number")
