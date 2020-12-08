
def tabela_hash(chaves, mod):
    tabela = {x: [] for x in range(mod)}

    for i in chaves:
        tabela[i % mod].append(str(i))

    return tabela


casos = int(input())

for i in range(casos):
    m, n = map(int, input().split())
    numeros = list(map(int, input().split()))

    numeros = tabela_hash(numeros, m)

    if i != 0:
        print()

    for j in range(m):
        if len(numeros[j]) > 0:
            print(f'{j} -> {" -> ".join(numeros[j])} -> \\')
        else:
            print(f'{j} -> \\')
    
