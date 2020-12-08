
casos = int(input())
espaco = input()

pular_linha = 1
i = 0

while i < casos:
    arvores = {}
    qtd_arvores = 0

    if i != (casos - 1):
        while True:
            especie = input()
            if especie == '':
                break
            
            qtd_arvores += 1

            if especie not in arvores:
                arvores[especie] = 1
            else:
                arvores[especie] += 1
    else:
        while True:
            try:
                especie = input()
            
                qtd_arvores += 1

                if especie not in arvores:
                    arvores[especie] = 1
                else:
                    arvores[especie] += 1
            except EOFError:
                break

    if pular_linha != 1:
        print()

    for tree in sorted(arvores):
        print(f'{tree} {arvores[tree] / qtd_arvores * 100 :.4f}')

    i += 1    
    pular_linha += 1
