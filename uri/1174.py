
vetor = []

for i in range(100):
    vetor.append(float(input()))

for i in range(len(vetor)):
    if vetor[i] <= 10:
        print('A[{}] = {:.1f}'.format(i, vetor[i]))
