
n = int(input())
resultado = 1

for i in range(n):
    numero, operador = input().split()

    if operador == '*':
        resultado *= int(numero)
    else:
        resultado /= int(numero)

print(f'{resultado :.0f}')
