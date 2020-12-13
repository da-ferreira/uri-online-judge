
texto = input().split()

for i in range(len(texto)):
    if len(texto[i]) >= 4:
        if texto[i][0:2] == texto[i][2:4]:
            texto[i] = texto[i][2:]

print(' '.join(texto))
