
from math import floor, sqrt

def eh_primo(numero):
    base = int(floor(sqrt(numero)))

    if numero in [0, 1]:
        return False

    for i in range(2, base + 1):
        if numero % i == 0:
            return False
    
    return True


quantidade = int(raw_input())
primos = set()

for i in range(quantidade):
    number = int(raw_input())

    if number not in primos:
        if eh_primo(number):
            primos.add(number)

primos = sorted(primos)

mostrar = ', '.join(str(x) for x in primos)

print(len(primos))

if len(primos) != 0:
    print mostrar + '.'
else:
    print
    