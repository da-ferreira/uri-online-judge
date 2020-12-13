
vogais = {
    '@': 'a', 
    '&': 'e',
    '!': 'i',
    '*': 'o',
    '#': 'u'
}

while True:
    try:
        mensagem = list(input())

        for i in range(len(mensagem)):
            if mensagem[i] in vogais:
                mensagem[i] = vogais[mensagem[i]]

        print(''.join(mensagem))
    except EOFError:
        break
