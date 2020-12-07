
from math import gcd, trunc

casos = int(input())

for i in range(casos):
    expressao = input().split()
    
    n1 = int(expressao[0])
    d1 = int(expressao[2])
    n2 = int(expressao[4])
    d2 = int(expressao[6])

    if expressao[3] == '+':
        numerador = (n1 * d2) + (n2 * d1)  
        denominador = d1 * d2

    elif expressao[3] == '-':
        numerador = (n1 * d2) - (n2 * d1)  
        denominador = d1 * d2

    elif expressao[3] == '*':
        numerador = n1 * n2  
        denominador = d1 * d2
    
    else:
        numerador = n1 * d2 
        denominador = n2 * d1

    mdc = gcd(numerador, denominador)
    
    print(f'{numerador}/{denominador} = {trunc(numerador / mdc)}/{trunc(denominador / mdc)}')
