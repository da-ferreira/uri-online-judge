
from math import sqrt, floor

def eh_primo(numero):
    base = floor(sqrt(numero))

    for i in range(2, base + 1):
        if numero % i == 0:
            return False

    return True


primo = int(input())
gemeos = []

while True:
    if eh_primo(primo):
        if eh_primo(primo - 2):
            gemeos.append(primo)
            gemeos.append(primo - 2)
            break
    
    primo -= 1

gemeos.sort()
print(gemeos[0], gemeos[1])
