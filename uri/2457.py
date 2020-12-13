
letra = input()
frase = input().split()

quantidade = 0

for palavra in frase:
    if letra in palavra:
        quantidade += 1

print('{:.1f}'.format((quantidade * 100) / len(frase)))
