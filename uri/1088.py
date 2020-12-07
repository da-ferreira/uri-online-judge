
def swaps(array):
    indice = movimentos = trocas = 0

    while indice < len(array):
        if array[indice] != indice + 1:
            temp2 = (array[indice] - indice) - 1
            movimentos += temp2
            movimentos += (temp2 - 1)
            
            temp = array[array[indice] - 1]

            array[array[indice] - 1] = array[indice]
            array[indice] = temp

            trocas += 2
        else:
            indice += 1

    if movimentos == (len(array) * (len(array) - 1) // 2):
        return movimentos
    
    return abs(movimentos - trocas)


while True:
    entrada = list(map(int, input().split()))
    if entrada[0] == 0:
        break

    quantidade = entrada.pop(0)
    count = swaps(entrada)

    if count % 2 == 0:
        print('Carlos')
    else:
        print('Marcelo')

