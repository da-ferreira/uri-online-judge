
from math import sqrt, floor

def max_prime(number):
    crivo = floor(sqrt(number))

    for i in range(2, crivo):
        if number % i == 0:
            return max_prime(number - 1)
    
    return number


rooms = int(input())

print(max_prime(rooms))
