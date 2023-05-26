def is_ugly(num):
        if num == 0:
            return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num /= i
        return num == 1

a=int(input())
if is_ugly(a)==True:
    print("Ugly Number")
else:
    print("Not Ugly Number")