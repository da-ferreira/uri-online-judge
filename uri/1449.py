
instancias = int(input())

for i in range(instancias):
    m, n = map(int, input().split())

    dicionario = {}

    for j in range(m):
        japones = input()
        portugues = input()

        dicionario[japones] = portugues

    for j in range(n):
        texto = input().split()

        for k in range(len(texto)):
            if texto[k] in dicionario:
                texto[k] = dicionario[texto[k]]

        print(' '.join(texto))
        
    print()
