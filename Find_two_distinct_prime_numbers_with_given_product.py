def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_factors(product):
    for i in range(2, int(product**0.5) + 1):
        if product % i == 0 and is_prime(i) and is_prime(product // i):
            return i, product // i
    return None

# Example usage
product = int(input())
prime_factors = find_prime_factors(product)
if prime_factors:
    prime1, prime2 = prime_factors
    print(prime1, prime2)
else:
    print("-1")
