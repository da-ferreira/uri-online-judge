
variaveis = {}
locador = []

while True:
    try:
        entrada = input().split()
    
        if len(entrada) == 3:
            variaveis[entrada[0]] = int(entrada[2])
            locador.append(entrada[0])
        else:
            if entrada[2].isalpha():
                temp = variaveis[entrada[2]]
            else:
                temp = int(entrada[2])

            if entrada[4].isalpha():
                temp2 = variaveis[entrada[4]]
            else:
                temp2 = int(entrada[4])
            
            variaveis[entrada[0]] = temp + temp2
            locador.append(entrada[0])
    except EOFError:
        break

print(variaveis[locador[-1]])
