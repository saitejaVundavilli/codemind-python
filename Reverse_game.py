def palindrome(x):
    rev=0
    temp=x
    while x!=0:
        d=x%10
        x=x//10
        rev=rev*10+d
    return rev
n=int(input())
lst=list(map(int,input().split()))
lst1=[palindrome(i) for i in lst]
print(*lst1)