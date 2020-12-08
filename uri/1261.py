
m, n = map(int, input().split())

palavras = {}

for i in range(m):
    entrada = input().split()
    palavras[entrada[0]] = int(entrada[1])

i = 0

while i < n:
    texto = []
    salario = 0

    while True:
        entrada = input()     
        if entrada != '' and entrada != '.':
            texto += entrada.split()
        else:
            if entrada == '.':
                break

    for j in texto:
        if j in palavras:
            salario += palavras[j]

    print(salario)
    i += 1       
