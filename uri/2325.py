
c, n = map(int, input().split())

programas_instalados = {}
internet = []

instalar = {}

for i in range(c):
    program, version = map(int, input().split())

    programas_instalados[program] = version

for i in range(n):
    program, version = map(int, input().split())

    internet.append([program, version])

internet.sort(key=lambda k: k[1], reverse=True)

for programa in internet:
    if programa[0] in programas_instalados:
        if programa[1] > programas_instalados[programa[0]]:

            instalar[programa[0]] = programa[1]
            programas_instalados[programa[0]] = programa[1]
    
    else:
        if programa[0] not in instalar:
            instalar[programa[0]] = programa[1]
            programas_instalados[programa[0]] = programa[1]
        else:
            if programa[1] > instalar[programa[0]]:
                instalar[programa[0]] = programa[1]
                programas_instalados[programa[0]] = programa[1]
   

for i in sorted(instalar):
    print(i, instalar[i])
