
casos = int(input())

for i in range(casos):
    jogador1 = input()
    jogador2 = input()

    if (jogador1 == 'ataque' and jogador2 == 'pedra') or (jogador1 == 'pedra' and jogador2 == 'papel') \
        or (jogador1 == 'ataque' and jogador2 == 'papel'):
        print('Jogador 1 venceu')

    elif (jogador1 == 'pedra' and jogador2 == 'ataque') or (jogador1 == 'papel' and jogador2 == 'pedra') \
        or (jogador1 == 'papel' and jogador2 == 'ataque'):
        print('Jogador 2 venceu')
    
    elif (jogador1 == 'papel' and jogador2 == 'papel'):
        print('Ambos venceram')
    
    elif (jogador1 == 'pedra' and jogador2 == 'pedra'):
        print('Sem ganhador')

    elif (jogador1 == 'ataque' and jogador2 == 'ataque'):
        print('Aniquilacao mutua')

    