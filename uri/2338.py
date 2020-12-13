
morse = {
    '=.===': 'a',
    '===.=.=.=': 'b',
    '===.=.===.=': 'c',
    '===.=.=': 'd',
    '=': 'e',
    '=.=.===.=': 'f',
    '===.===.=': 'g',
    '=.=.=.=': 'h',
    '=.=': 'i',
    '=.===.===.===': 'j',
    '===.=.===': 'k',
    '=.===.=.=': 'l',
    '===.===': 'm',
    '===.=': 'n',
    '===.===.===': 'o',
    '=.===.===.=': 'p',
    '===.===.=.===': 'q',
    '=.===.=': 'r',
    '=.=.=': 's',
    '===': 't',
    '=.=.===': 'u',
    '=.=.=.===': 'v',
    '=.===.===': 'w',
    '===.=.=.===': 'x',
    '===.=.===.===': 'y',
    '===.===.=.=': 'z'
}

casos = int(input())

for i in range(casos):
    texto_morse = input()
    mensagem = ''

    texto_morse = texto_morse.split('.......') 

    for j in range(len(texto_morse)):
        temp = texto_morse[j].split('...')

        for k in range(len(temp)):
            mensagem += morse[temp[k]]

        if j != (len(texto_morse) - 1):
            mensagem += ' '

    print(mensagem)
