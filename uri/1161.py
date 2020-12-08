
from math import factorial

while True:
    try:
        valores = input().split()

        m = int(valores[0])
        n = int(valores[1])
        print(factorial(m) + factorial(n))
    except:
        break
