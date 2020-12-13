
n = int(input())

hexadecimais = input().split()
frase = ''

for letra in hexadecimais:
    frase += chr(int(letra, 16))

print(frase)
