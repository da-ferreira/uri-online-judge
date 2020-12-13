
instancias = int(input())

for i in range(instancias):
    numero = int(input())
    regioes = (((numero + 1) ** 2) - (numero + 1) + 2) / 2

    print(int(regioes))
