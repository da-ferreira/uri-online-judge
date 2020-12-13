
casos = int(input())

for i in range(casos):
    qtd = int(input())
    idiomas = []

    for j in range(qtd):
        idiomas.append(input())

    if idiomas.count(idiomas[0]) == len(idiomas):
        print(idiomas[0])
    else:
        print('ingles')
    