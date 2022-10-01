a=int(input())
sq=a*a
le=len(str(a))
last=sq%(10**le)
if last==a:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")