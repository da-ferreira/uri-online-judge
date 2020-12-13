
def eh_primo(numero):
    from math import floor, sqrt

    for i in range(2, floor(sqrt(numero))):
        if numero % i == 0:
            return False

    return True


selos = int(input())

if selos < 4:
    print('N')
else:
    if selos % 2 == 0:
        print('S')
    else:
        if eh_primo(selos):
            print('N')
        else:
            print('S')
