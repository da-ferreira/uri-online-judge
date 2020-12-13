
def eh_primo(numero):
    from math import floor, sqrt

    for i in range(2, floor(sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    
    return True


casos = int(input())

for i in range(casos):
    number = int(input())
    number += 1

    if number % 7 == 0:   
        if number % 2 == 1:
            if eh_primo(number + 2):
                print('Yes')
            else:
                print('No')
        else:
            print('No')
    else:
        print('No')
    
