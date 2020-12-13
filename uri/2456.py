
sequencia = list(map(int, input().split()))

crescente = decrescente = 0

for i in range(1, len(sequencia)):
    
    if sequencia[i] > sequencia[i - 1]:
        crescente += 1
    
    elif sequencia[i] < sequencia[i - 1]:
        decrescente += 1

if crescente == (len(sequencia) - 1):
    print('C')
elif decrescente == (len(sequencia) - 1):
    print('D')
else:
    print('N')
