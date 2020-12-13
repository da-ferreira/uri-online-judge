
from math import sqrt, floor

def eh_primo(numero):
    for i in range(2, floor(sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    return True


numero = int(input())
primos = []

while len(primos) != 10:
    if eh_primo(numero):
        primos.append(numero)
    
    numero += 1


print(f'{sum(primos)} km/h')

horas = 60000000 // sum(primos)

print(f'{horas} h / {horas // 24} d')
