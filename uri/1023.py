
from math import floor

linha = 1

while True:
    n = int(input())
    if n == 0:
        break
    
    if linha != 1:
        print()

    consumo_medio = [0, 0]
    pessoas_e_consumo = {}

    for i in range(n):
        moradores, consumo = map(int, input().split())

        if floor(consumo / moradores) not in pessoas_e_consumo:
            pessoas_e_consumo[floor(consumo / moradores)] = moradores
        else:
            pessoas_e_consumo[floor(consumo / moradores)] += moradores

        consumo_medio[0] += moradores 
        consumo_medio[1] += consumo

    temp = len(pessoas_e_consumo)

    print(f'Cidade# {linha}:')

    for i in sorted(pessoas_e_consumo):
        if temp != 1:
                print(f'{pessoas_e_consumo[i]}-{i}', end=' ')
        else:
            print(f'{pessoas_e_consumo[i]}-{i}')
        
        temp -= 1
    
    media = f'{consumo_medio[1] / consumo_medio[0] :.10f}'
    media = media[0:media.index('.') + 3]

    print(f'Consumo medio: {media} m3.')

    linha += 1
