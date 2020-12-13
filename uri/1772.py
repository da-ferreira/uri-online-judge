
while True:        
    numero, permutacoes = map(int, input().split())
    if numero == 0 and permutacoes == 0:
        break

    numero = bin(numero)[2:]
    maior = int(numero, 2)
    menor = int(numero, 2)
    ultimo = 0

    numero = numero.zfill(32)

    for i in range(permutacoes):
        a, b = map(int, input().split())
        
        numero = list(numero)
        
        if a > b:
            b, a = a, b

        numero[len(numero) - b - 1], numero[len(numero) - a - 1] = numero[len(numero) - a - 1], numero[len(numero) - b - 1]

        numero = ''.join(numero)

        if int(numero, 2) > maior:
            maior = int(numero, 2)
        
        if int(numero, 2) < menor:
            menor = int(numero, 2)
        
        if i == permutacoes - 1:
            ultimo = int(numero, 2)
    
    print(f'{ultimo} {maior} {menor}')
