
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    ninguem_revolveu_todos =  0 # 
    resolvido_por_1_pessoa = 0 #
    nenhum_resolvido_por_todos = 0 #
    todos_resolveram_1 = 0 #

    participantes = []
    pontos = 0

    for i in range(n):
        participantes.append(input().split())
    
    for i in range(n):
        if '0' in participantes[i]:
            ninguem_revolveu_todos += 1
        
        if '1' in participantes[i]:
            todos_resolveram_1 += 1

    nenhum_resolvido_por_todos2 = resolvido_por_1_pessoa2 = True

    for i in range(m):
        for j in range(n):
            if participantes[j][i] == '1':
                nenhum_resolvido_por_todos += 1
            if participantes[j][i] == '0':
                resolvido_por_1_pessoa += 1
        
        if nenhum_resolvido_por_todos == n:
            nenhum_resolvido_por_todos2 = False
        nenhum_resolvido_por_todos = 0

        if resolvido_por_1_pessoa == n:
            resolvido_por_1_pessoa2 = False
        resolvido_por_1_pessoa = 0

    if ninguem_revolveu_todos == n:
        pontos += 1
    if todos_resolveram_1 == n:
        pontos += 1
    if nenhum_resolvido_por_todos2:
        pontos += 1
    if resolvido_por_1_pessoa2:
        pontos += 1
    
    print(pontos)
