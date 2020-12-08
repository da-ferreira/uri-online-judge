
soma = qtd_amigos = 0
while True:
    try:
        amigos = input()
        distancia = int(input())

        soma += distancia
        qtd_amigos += 1
    except EOFError:
        media = soma / qtd_amigos
        print('{:.1f}'.format(media))
        break
