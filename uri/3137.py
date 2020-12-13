
paginas = int(input())
digitos = 0

for i in range(1, paginas + 1):
    digitos += len(str(i))

print(digitos)
