
from math import ceil

casos = int(input())

for i in range(casos):
    quantidade = int(input())
    pesos_presentes = {}

    for j in range(quantidade):
        nome = input()
        peso = float(input())
        pesos_presentes[nome] = peso

    peso_treno = float(input())
    nao_listado = []
    peso_total = 0

    while True:
        nome_presente = input() 
        qtd = int(input())

        if nome_presente == '-' and qtd == 0:
            break

        if nome_presente not in pesos_presentes:
            nao_listado.append(nome_presente)
        else:
            peso_total += (pesos_presentes[nome_presente] * qtd)

    for j in range(len(nao_listado)):
        print(f'NAO LISTADO: {nao_listado[j]}')

    print(f'Peso total: {peso_total :.2f} kg')
    print(f'Numero de trenos: {ceil(peso_total / peso_treno)}')      
    print()
