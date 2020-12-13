
casos = int(input())

for i in range(casos):
    expressao = input()

    int1 = int(expressao[0:expressao.index(' ')])
    operador = expressao[expressao.index(' ')+1:expressao.index(' ')+2]
    int2 = int(expressao[expressao.index(operador)+1:expressao.index('=')])
    resultado = int(expressao[expressao.index('=')+1:])

    if operador == '+':
        result_certo = int1 + int2
    elif operador == '-':
        result_certo = int1 - int2
    elif operador == 'x':
        result_certo = int1 * int2

    vezes = abs(result_certo - resultado)

    print('E' + 'r' * vezes + 'ou!')
