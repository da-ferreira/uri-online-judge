
from math import sqrt

def delta(a, b, c):

    x1 = (-b + sqrt((b) ** 2 - 4 * a * c)) // 2

    x2 = (-b - sqrt((b) ** 2 - 4 * a * c)) // 2

    return [x1, x2]


casos = int(input())

for i in range(casos):
    n = int(input())
    n = n * 2

    linhas = delta(1, 1,  -n)

    print(int(max(linhas)))
