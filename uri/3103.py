casos = int(input())

for i in range(casos):
    numero = input().strip()
    numero = list(numero)
    numero.sort()

    if numero[0] == '0':
        for i in range(len(numero)):
            if numero[i] != '0':
                temp = numero[i]
                numero.pop(i)
                numero.insert(0, temp)
                break
    
    print(''.join(numero))
