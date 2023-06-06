import math

def square(n):
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n
a=int(input())
print(square(a))