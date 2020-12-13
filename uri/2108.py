
maior_palavra = [0, '']
while True:
    string = input().split()
    if string[0] == '0':
        break

    caracteres = []

    for palavra in string:
        caracteres.append(len(palavra))
        if len(palavra) >= maior_palavra[0]:
            maior_palavra[0] = len(palavra)
            maior_palavra[1] = palavra
    
    for i in range(len(caracteres)):
        if i != (len(caracteres) - 1):
            print(caracteres[i], end='-')
        else:
            print(caracteres[i])

print('\nThe biggest word: {}'.format(maior_palavra[1]))
