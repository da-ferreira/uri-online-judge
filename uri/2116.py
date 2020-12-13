
from math import sqrt, floor

def eh_primo(numero):
    piso_sqrt = floor(sqrt(numero))
    divisores = 0
    
    for i in range(1, piso_sqrt+1):
        if numero % i == 0:
            divisores += 1
    if divisores == 1 and numero not in [0, 1]:
        return True
    else:
        return False


n, m = map(int, input().split())

for i in range(n, -1, -1):
    if eh_primo(i):
        n = i
        break

for i in range(m, -1, -1):
    if eh_primo(i):
        m = i
        break

print(n * m) 
