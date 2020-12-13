
numero = float(input())
numero = f'{numero :.4e}'
numero = numero.replace('e', 'E')

if numero[0] != '-':
    print(f'+{numero}')
else:
    print(numero)
