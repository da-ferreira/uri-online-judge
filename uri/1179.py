
pares = []
impares = []

for i in range(15):
    num = int(input())

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    
    if len(pares) == 5:
        for j in range(5):
            print('par[{}] = {}'.format(j, pares[j]))
        pares.clear()

    if len(impares) == 5:
        for j in range(5):
            print('impar[{}] = {}'.format(j, impares[j]))
        impares.clear()
    
for i in range(len(impares)):
    print('impar[{}] = {}'.format(i, impares[i]))
for i in range(len(pares)):
    print('par[{}] = {}'.format(i, pares[i]))
