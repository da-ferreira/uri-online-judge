
from math import gcd

while True:
    try:
        valores = list(map(int, input().split()))
        
        maior = max(valores)
        valores.remove(maior)

        if ((valores[0] ** 2) + (valores[1] ** 2)) == maior ** 2:
            if gcd(valores[0], valores[1]) == 1:
                print('tripla pitagorica primitiva')
            else:
                print('tripla pitagorica')
        else:
            print('tripla')
    except EOFError:
        break
