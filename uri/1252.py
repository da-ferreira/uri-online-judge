
from math import inf  # infinito

while True:
    n, modulo = map(int, input().split())
    if n == 0 and modulo == 0:
        print(0, 0)
        break

    numeros = []

    for i in range(n):
        number = int(input())

        if number < 0:
            mod = (abs(number) % modulo) * -1
        else:
            mod = number % modulo 

        if number % 2 == 0:
            impar_ou_par = 'par'

            empate_par = number
            empate_impar = 0
        else:
            impar_ou_par = 'impar'
            
            empate_impar = number
            empate_par = inf
        
        numeros.append([number, mod, impar_ou_par, empate_impar, empate_par])
    
    numeros = sorted(numeros, key=lambda k: k[4])
    numeros = sorted(numeros, key=lambda k: k[3], reverse=True)
    numeros = sorted(numeros, key=lambda k: k[2])
    numeros = sorted(numeros, key=lambda k: k[1])

    print(n, modulo)

    for i in range(n):
        print(numeros[i][0])
