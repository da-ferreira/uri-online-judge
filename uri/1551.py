
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
casos = int(input())

for i in range(casos):
    frase = input()
    quantidade = 0

    for letter in alfabeto:
        if letter in frase:
            quantidade += 1
    
    if quantidade == 26:
        print('frase completa')
    elif quantidade >= 13:
        print('frase quase completa')
    else:
        print('frase mal elaborada')
