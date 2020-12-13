
limit_overflow = int(input())

int1, operador, int2 = input().split()

if operador == '+':
    resultado = int(int1) + int(int2)
else:
    resultado = int(int1) * int(int2)

if resultado > limit_overflow:
    print('OVERFLOW')
else:
    print('OK')
