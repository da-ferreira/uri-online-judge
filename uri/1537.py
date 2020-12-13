
from math import factorial

while True:
    pessoas = int(input())
    if pessoas == 0:
        break

    maneiras = factorial(pessoas) // factorial(3)

    print(maneiras % 1000000009)
