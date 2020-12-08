
def ultrapassagens(largada, chegada, tamanho):
    overtaking = 0

    for i in range(tamanho):
        j = chegada[i]

        while largada[i] != j:
            item = largada.index(j)
            item_atras = largada.index(j) - 1

            largada[item], largada[item_atras] = largada[item_atras], largada[item]
            overtaking += 1

    return overtaking


while True:
    try:
        n = int(input())
        
        larg = list(map(int, input().split()))
        cheg = list(map(int, input().split()))

        print(ultrapassagens(larg, cheg, n))
    except EOFError:
        break
