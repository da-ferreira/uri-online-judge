
casos = int(input())

sequencia = [1, 9]

for i in range(casos):
    numero = int(input())
    print(sequencia[numero % 2])
