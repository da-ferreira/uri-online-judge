
j = 1
while True:
    quantidade = int(input())
    if quantidade == 0:
        break
    
    palavras = []
    maior = 0
    for i in range(quantidade):
        palavras.append(input())
        
        if len(palavras[-1]) > maior:
            maior = len(palavras[-1])

    if j != 1:
        print()

    for word in palavras:
        print(word.rjust(maior))
    j = 2

