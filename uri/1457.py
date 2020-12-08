
casos = int(input())

for i in range(casos):
    numero = input()
    k = numero.count('!')
    numero = int(numero.replace('!', ''))

    fatorial = numero
    numero -= k        
    
    while numero >= 1:
        fatorial *= numero
        numero -= k        
    
    print(fatorial)
