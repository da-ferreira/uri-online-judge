
def sapos_na_pedra(posicao_sapo, salto, pedras_do_rio):
    pedras_do_rio[posicao_sapo] = 1
    
    tamanho = len(pedras) - 1
    pra_frente = posicao_sapo
    pra_tras = posicao_sapo

    while pra_frente + salto <= tamanho:
        pra_frente += salto
        pedras_do_rio[pra_frente] = 1

    while pra_tras - salto >= 0:
        pra_tras -= salto
        pedras_do_rio[pra_tras] = 1
    
    return pedras_do_rio


n, sapos = map(int, input().split())
pedras = [0] * n

for i in range(sapos):
    inicial, pulo = map(int, input().split())

    pedras = sapos_na_pedra(inicial - 1, pulo, pedras)

for i in pedras:
    print(i)
