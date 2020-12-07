
casos = int(input())

for i in range(casos):
    expressao = input().replace('.', '')
    
    diamantes = 0
    pilha = []

    for caracter in expressao:
        if caracter == '<':
            pilha.append(caracter)
        elif caracter == '>' and len(pilha) > 0:
            pilha.remove('<')
            diamantes += 1

    print(diamantes)
