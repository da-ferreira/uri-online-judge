

def maior_numero(numero):
    numero = list(str(numero))
    numero.sort(reverse=True)

    numero = ''.join(numero)
    return int(numero)


def menor_numero(numero):
    numero = list(str(numero))
    numero.sort()

    numero = ''.join(numero)
    return int(numero)


casos = int(input())

for i in range(casos):
    numero = input()

    while len(numero) < 4:
        numero = '0' + numero    
    
    contagem = 0

    while numero != '6174':
        while len(numero) < 4:
            numero = '0' + numero

        if len(set(numero)) == 1:
            contagem = -1
            break
        
        numero = str(maior_numero(numero) - menor_numero(numero))
        contagem += 1
    
    print(f'Caso #{i + 1}: {contagem}')
