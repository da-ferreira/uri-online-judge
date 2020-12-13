
padrao = {
    'GQaku': '0',
    'ISblv': '1',
    'EOYcmw': '2',
    'FPZdnx': '3',
    'JTeoy': '4',
    'DNXfpz': '5',
    'AKUgq': '6',
    'CMWhr': '7',
    'BLVis': '8',
    'HRjt': '9'
}

casos = int(input())

for i in range(casos):
    senha = input()
    senha = senha.replace(' ', '')

    password_encrypted = ''

    for j in range(12):
        for chave in padrao.keys():
            if senha[j] in chave:
                password_encrypted += padrao[chave]

    print(password_encrypted)
