
def busca_binaria(vetor, item):
    inicio = 0
    fim = len(vetor) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if vetor[meio] == item:
            return meio

        elif item < vetor[meio]:
            fim = meio - 1
        
        elif item > vetor [meio]:
            inicio = meio + 1


qtd_casas, qtd_encomendas = map(int, input().split())

casas = list(map(int, input().split()))
encomendas = list(map(int, input().split()))

posicao_carteiro = 0
tempo = 0

for i in range(qtd_encomendas):
    house = busca_binaria(casas, encomendas[i])
    tempo += abs(posicao_carteiro - house)

    posicao_carteiro = house

print(tempo)
