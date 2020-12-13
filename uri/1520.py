
def busca_binaria(vetor, item):
    inicio = 0
    fim = len(vetor) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if vetor[meio] == item:
            while (meio != 0) and vetor[meio - 1] == item:
                meio -= 1

            comeco = meio  # primeira posicao do item procurado

            while (len(vetor) - 1) != meio and vetor[meio + 1] == item:
                meio += 1

            return (comeco, meio)  # ultima posicao do item procurado

        elif item < vetor[meio]:    
            fim = meio - 1

        elif item > vetor [meio]:
            inicio = meio + 1

    return None


while True:
    try:
        qtd_caixas = int(input())
    except EOFError:
        break
    except:
        continue
    
    caixas = []

    for i in range(qtd_caixas):
        x, y = map(int, input().split())
        temp = [num for num in range(x, y + 1)]

        caixas += temp

    caixas.sort()

    consulta = int(input())
    posicoes = busca_binaria(caixas, consulta)

    if posicoes is None:
        print(f'{consulta} not found')
    else:
        print(f'{consulta} found from {posicoes[0]} to {posicoes[1]}')
