
def swaps(array):
    indice = 0
    trocas = 0

    while indice < len(array):
        if array[indice] != indice + 1:
            temp = array[array[indice] - 1]

            array[array[indice] - 1] = array[indice]
            array[indice] = temp
            
            trocas += 1
        else:
            indice += 1

    return trocas


casos = int(input())

for i in range(casos):
    quantidade = int(input())
    numeros = list(map(int, input().split()))

    print(swaps(numeros))

