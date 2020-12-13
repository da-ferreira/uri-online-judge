
def kamenetsky(number):
    """
    Formula de kamenetsky permite saber quantos
    digitos tem o fatorial de um numero qualquer > 0
    se calcular seu fatorial.

    :param number: O numero do fatorial
    :return: Quantidade de digitos do fatorial desse numero.
    """
    
    import math

    if number < 0:  # nao existe
        return 0
    
    elif number <= 1:
        return 1
    
    digits = (number * math.log10(number / math.e)) + (math.log10(2 * math.pi * number) / 2)
   
    return math.floor(digits) + 1


n = int(input())
print(kamenetsky(n))
