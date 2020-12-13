
from math import factorial

casos = int(input())
vencedores = []

for i in range(casos):
    lucas = list(map(int, input().split('^')))
    pedro = input()[0:-1]

    if (lucas[0] ** lucas[1]) > factorial(int(pedro)):
        vencedores.append('Lucas')
    else:
        vencedores.append('Pedro')

if vencedores.count('Lucas') > vencedores.count('Pedro'):
    print('Campeao: Lucas!')
elif vencedores.count('Lucas') < vencedores.count('Pedro'):
    print('Campeao: Pedro!')
else:
    print('A competicao terminou empatada!')

for i in range(1, casos+1):
    print(f'Rodada #{i}: {vencedores[i - 1]} foi o vencedor')
