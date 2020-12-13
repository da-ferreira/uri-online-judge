
casos = int(input())

for i in range(casos):
    numero = int(input())
    numero = bin(numero)

    print(numero.count('1'))
