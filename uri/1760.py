
from math import sqrt

while True:
    try:
        lado = int(input())
        fractal = (2 * sqrt(3) * lado ** 2) / 5
        
        print(f'{fractal :.2f}')
    except EOFError:
        break
