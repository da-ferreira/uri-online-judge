
from math import sqrt, floor

def eh_primo(numero):
    piso_sqrt = floor(sqrt(numero))
    
    for i in range(2, piso_sqrt+1):
        if numero % i == 0:
            return False
    return True


def gera_proximo_primo(prime):
    prime += 1
    
    while not eh_primo(prime):
        prime += 1
    return prime - 1


while True:
    pessoas = int(input())
    if pessoas == 0:
        break

    pessoas = [x for x in range(1, pessoas + 1)]

    i = 1
    primo = 1
    while len(pessoas) != 1:
        pessoas.pop(i)

        primo = gera_proximo_primo(primo + 1)
        i = (i + primo) % len(pessoas)

    print(pessoas[0])
