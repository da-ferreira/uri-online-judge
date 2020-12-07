
casos = int(input())

caso = 1

for i in range(casos):
    numeros = list(map(int, input().split()))
    quantidade = numeros.pop(0)

    numeros.sort()
    permutacao = []

    j = 0
    k = quantidade - 1
    alterna = True

    while j < quantidade // 2:
        if alterna:
            permutacao.insert(0, numeros[j])
            permutacao.append(numeros[k])
            alterna = False
        else:
            permutacao.append(numeros[j])
            permutacao.insert(0, numeros[k])
            alterna = True
        
        j += 1
        k -= 1

    # Há casos de quantidade impar que quando colocar o numero que sobra no final
    # da o maior resultado e outros casos só da o maior se colocar no começo.
    # Entao, tive que criar duas listas com essas opções e pegar o maior valor.

    soma = 0

    if quantidade % 2 == 1:
        if abs(numeros[quantidade // 2] - permutacao[0]) >= abs(numeros[quantidade // 2] - permutacao[-1]): 
            permutacao.insert(0, numeros[quantidade // 2])
        else:
            permutacao.append(numeros[quantidade // 2])
    
    for j in range(quantidade - 1):
        soma += abs(permutacao[j] - permutacao[j + 1])

    print(f'Case {caso}: {soma}') 

    caso += 1
