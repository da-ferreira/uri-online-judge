
soma = 0
valores = [int(input()), int(input())]
valores.sort()

for i in range(valores[0], valores[1]+1):
    if i % 13 != 0:
        soma += i
print(soma)
