
from math import factorial

n = int(input())
soma = 0

acumulado = {}

for i in range(n):
    cor, baloes = input().split()
    
    soma += int(baloes) 
    
    if cor not in acumulado:
        acumulado[cor] = int(baloes)
    else:
        acumulado[cor] += int(baloes)

k = 1

for x in acumulado:
    k *= factorial(acumulado[x])

print('Feliz aniversario Tobias!')
print(int(factorial(soma) / k))
