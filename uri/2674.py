
from math import sqrt, floor


def eh_primo(numero):
    numero = int(numero)
    piso_sqrt = floor(sqrt(numero))
    divisores = 0
    
    for i in range(1, piso_sqrt+1):
        if numero % i == 0:
            divisores += 1
    if divisores == 1 and numero not in [0, 1]:
        return True
    else:
        return False

while True:
    try:        
        num = int(input())
        
        if eh_primo(num):
            digitos = 0
            for i in range(len(str(num))):
                if eh_primo(str(num)[i]):
                    digitos += 1
            
            if digitos == len(str(num)):
                print('Super')
            else:
                print('Primo')
        else:
            print('Nada')
    except EOFError:
        break
