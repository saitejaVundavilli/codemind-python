def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def find_closest_prime(num):
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
    diff_smaller = abs(num - smaller)
    diff_larger = abs(larger - num)
    if diff_smaller <= diff_larger:
        return  diff_smaller
    else:
        return diff_larger
number = int(input())
if is_prime(number):
    print(0)
else:
    difference = find_closest_prime(number)
    print(difference)
