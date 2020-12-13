
def quantos_divisores(num):
    divisores = 1
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            divisores += 1
    
    if divisores % 2 == 0:
        return False
    else:
        return True


casos = int(input())

for i in range(casos):
    numero = int(input())

    for j in range(1, numero + 1):
        if quantos_divisores(j):
            numero -= 1
    print(numero)
