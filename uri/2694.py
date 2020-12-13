
casos = int(input())

for i in range(casos):
    caracteres = input()
    numero = [int(caracteres[2:4])]
    numero.append(int(caracteres[5:8]))
    numero.append(int(caracteres[11:13]))
    print(sum(numero))
