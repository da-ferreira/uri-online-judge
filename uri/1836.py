
from math import sqrt

def vitalidade(hp, iv, ev, level):
    result = ((iv + hp + (sqrt(ev) / 8) + 50) * level) // 50 + 10

    return int(result)


def atributos(level, bs, iv, ev):
    result = ((iv + bs + (sqrt(ev) / 8)) * level) // 50 + 5

    return int(result)


casos = int(input())

for i in range(casos):
    nome, level = input().split()
    level = int(level)

    hp = list(map(int, input().split()))
    at = list(map(int, input().split()))
    df = list(map(int, input().split()))
    sp = list(map(int, input().split()))

    print(f'Caso #{i + 1}: {nome} nivel {level}')
    print(f'HP: {vitalidade(hp[0], hp[1], hp[2], level)}')
    print(f'AT: {atributos(level, at[0], at[1], at[2])}')
    print(f'DF: {atributos(level, df[0], df[1], df[2])}')
    print(f'SP: {atributos(level, sp[0], sp[1], sp[2])}')
    