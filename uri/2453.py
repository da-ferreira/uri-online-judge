
texto = input()
alterna = True

result = ''

for letra in texto:
    if letra.casefold() == 'p' and alterna:
        alterna = False
    else:
        result += letra
        alterna = True

print(result) 
