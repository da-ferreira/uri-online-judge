
sobrescritas = int(input())

arquivo_antes = input()
arquivo_depois = input()

certo = True

if sobrescritas % 2 == 0:
    for i in range(len(arquivo_depois)):
        if arquivo_depois[i] != arquivo_antes[i]:
            certo = False
            break
else:
    for i in range(len(arquivo_depois)):
        if arquivo_depois[i] == '1':
            if arquivo_antes[i] == '1':
                certo = False
                break
        else:
            if arquivo_antes[i] == '0':
                certo = False
                break

if certo:
    print("Deletion succeeded")
else:
    print("Deletion failed")
