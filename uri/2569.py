
a, operador, b = input().split()

a = a.replace('7', '0')
b = b.replace('7', '0')

if operador == '+':
    resultado = int(a) + int(b)
else:
    resultado = int(a) * int(b)

resultado = str(resultado)
print(int(resultado.replace('7', '0')))
