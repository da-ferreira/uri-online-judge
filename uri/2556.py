
while True:
    try:
        quantidade = int(input())
        numeros = list(map(int, input().split()))
        numeros.sort()

        if quantidade % 2 == 1:
            numeros.pop()
            quantidade -= 1
        
        convidados = quantidade // 2
        minutos = numeros[quantidade // 2] - numeros[quantidade // 2 - 1]

        print(convidados, minutos)
    except EOFError:
        break
