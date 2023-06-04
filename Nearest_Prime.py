def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def find_nearest_prime(num):
    if is_prime(num):
        return num
    smaller = larger = num
    while True:
        smaller -= 1
        if is_prime(smaller):
            break
    while True:
        larger += 1
        if is_prime(larger):
            break
    if num - smaller <= larger - num:
        return smaller
    else:
        return larger
number = int(input())
for i in range(number):
    nearest_prime = find_nearest_prime(int(input()))
    print( nearest_prime)
