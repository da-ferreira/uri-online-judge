
i = 1
while True:
    m = int(input())
    if m == 0:
        break

    expressao = input()

    soma = 0
    operador = temp = ''

    for j in range(len(expressao)):
        if operador == '':
            if j == 0:
                temp += expressao[j]
            else:
                if expressao[j] not in '+-':
                    temp += expressao[j]
                else:
                    operador = expressao[j]
                    soma = int(temp)
                    temp = ''
        else:
            if expressao[j] not in '+-':
                temp += expressao[j]
            else:
                if operador == '-':
                    soma -= int(temp)
                else:
                    soma += int(temp)
                
                temp = ''
                operador = expressao[j]
    
    if operador == '-':
        soma -= int(temp)
    else:
        soma += int(temp) 

    print(f'Teste {i}')
    print(soma)
    print()

    i += 1
