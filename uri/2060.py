
dois = tres = quatro = cinco = 0

quantidade = int(input())
numeros = input().split()

for i in range(quantidade):
    if int(numeros[i]) % 2 == 0:
        dois += 1
    if int(numeros[i]) % 3 == 0:
        tres += 1
    if int(numeros[i]) % 4 == 0:
        quatro += 1
    if int(numeros[i]) % 5 == 0:
        cinco += 1
    
print('{} Multiplo(s) de 2'.format(dois))
print('{} Multiplo(s) de 3'.format(tres))
print('{} Multiplo(s) de 4'.format(quatro))
print('{} Multiplo(s) de 5'.format(cinco))
