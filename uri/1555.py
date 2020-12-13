
def rafael(x, y):
    resultado = ((3 * x) ** 2) + y ** 2
    return resultado


def beto(x, y):
    resultado = (2 * (x ** 2)) + ((5 * y) ** 2)
    return resultado


def carlos(x, y):
    resultado = (-100 * x) + (y ** 3)
    return resultado


casos = int(input())

for i in range(casos):
    numeros = input().split()
    x = int(numeros[0])
    y = int(numeros[1])

    amigos = [rafael(x, y), beto(x, y), carlos(x, y)]
    
    if amigos[0] is max(amigos):
        print('Rafael ganhou')
    elif amigos[1] is max(amigos):
        print('Beto ganhou')
    else:
        print('Carlos ganhou')
