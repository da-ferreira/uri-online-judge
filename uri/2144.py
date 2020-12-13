
media_geral = [0, 0]

while True:
    w1, w2, r = map(int, input().split())
    if r == 0:
        break

    esquerdo = w1 * (1 + (r / 30))
    direito = w2 * (1 + (r / 30))

    media = (esquerdo + direito) / 2
    
    media_geral[0] += media
    media_geral[1] += 1
    
    if media >= 1 and media < 13:
        print('Nao vai da nao')
    elif media >= 13 and media < 14:
        print('E 13')
    elif media >= 14 and media < 40:
        print('Bora, hora do show! BIIR!')
    elif media >= 40 and media <= 60:
        print('Ta saindo da jaula o monstro!')
    else:
        print('AQUI E BODYBUILDER!!')
    
if media_geral[0] / media_geral[1] > 40:
    print('\nAqui nois constroi fibra rapaz! Nao e agua com musculo!')
