
while True:
    quantidade = int(input())
    if quantidade == 0:
        break

    comandos = input()
    soldado = 'N'

    for posicao in comandos:
        if (soldado == 'N' and posicao == 'D') or (soldado == 'S' and posicao == 'E'):
            soldado = 'L'

        elif (soldado == 'N' and posicao == 'E') or (soldado == 'S' and posicao == 'D'):
            soldado = 'O'

        elif (soldado == 'L' and posicao == 'D') or (soldado == 'O' and posicao == 'E'):
            soldado = 'S'

        elif (soldado == 'L' and posicao == 'E') or (soldado == 'O' and posicao == 'D'):
            soldado = 'N' 

    print(soldado)
