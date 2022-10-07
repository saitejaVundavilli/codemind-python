a=int(input())
word=str(a)
leng=len(word)
first=word[0]
if(first==0 or leng!=10):
    print("Invalid")
else:
    print("Valid")