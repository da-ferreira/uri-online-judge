
casos = int(input())
vetor = input().split()

for i in range(len(vetor)):
    vetor[i] = int(vetor[i])

menor = min(vetor)
print('Menor valor: {}'.format(menor))
print('Posicao: {}'.format(vetor.index(menor)))
