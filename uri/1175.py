
vetor = []

for i in range(20):
    vetor.append(int(input()))

j = 19
for i in range(10):
    primeiro = vetor[i]
    ultimo = vetor[j]

    vetor[i] = ultimo
    vetor[j] = primeiro

    j -= 1

for i in range(len(vetor)):
    print('N[{}] = {}'.format(i, vetor[i]))
