
casos = int(input())

for i in range(casos):
    texto = list(input())
    
    for i in range(len(texto)):
        if texto[i].isalpha():
            texto[i] = chr(ord(texto[i]) + 3)
    
    texto = texto[-1::-1]
    metade = len(texto) // 2

    for j in range(metade, len(texto)):
        texto[j] = chr(ord(texto[j]) - 1)
    
    print(''.join(texto))
