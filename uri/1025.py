
def busca_binaria(vetor, item):
    inicio = 0
    fim = len(vetor) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if vetor[meio] == item:
            while vetor[meio - 1] == item:
                meio -= 1
            return meio + 1
            
        elif item < vetor[meio]:
            fim = meio - 1
        
        elif item > vetor [meio]:
            inicio = meio + 1

    return None  # caso a lista for invalida
    
i = 1
while True:
    n, querys = map(int, input().split())
    if n == 0 and querys == 0:
        break
    
    marmores = []

    for j in range(n):
        marmores.append(int(input()))
    
    marmores.sort()

    print(f'CASE# {i}:')

    for j in range(querys):
        consulta = int(input())
        indice = busca_binaria(marmores, consulta)

        if indice is None:
            print(f'{consulta} not found')
        else:
            print(f'{consulta} found at {indice}')

    i += 1
