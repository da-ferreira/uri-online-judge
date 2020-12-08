
def eh_do_mesmo_grupo(n1, n2):

    n1 = int(n1[::-1])
    n2 = int(n2[::-1])

    for i in range(1, 96, 4):
        if n1 in range(i, i + 4) and n2 in range(i, i + 4):
            return True

    if n1 in [97, 98, 99, 0] and n2 in [97, 98, 99, 0]:
        return True
    
    return False


while True:
    entrada = input().split()

    valor_aposta = float(entrada[0])
    n_escolhido = entrada[1]
    n_sorteado = entrada[2]

    if valor_aposta == 0 and n_escolhido == '0' and n_sorteado == '0':
        break

    n_escolhido = n_escolhido.zfill(4)    
    n_sorteado = n_sorteado.zfill(4)

    if n_escolhido[-1:-5:-1] == n_sorteado[-1:-5:-1]:
        valor_aposta *= 3000
    
    elif n_escolhido[-1:-4:-1] == n_sorteado[-1:-4:-1]:
        valor_aposta *= 500
    
    elif n_escolhido[-1:-3:-1] == n_sorteado[-1:-3:-1]:
        valor_aposta *= 50
    
    elif eh_do_mesmo_grupo(n_escolhido[-1:-3:-1], n_sorteado[-1:-3:-1]):
        valor_aposta *= 16
    
    else:
        valor_aposta = 0.0
    
    print(f'{valor_aposta :.2f}')
