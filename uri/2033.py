
while True:
    try:
        emprestimo = float(input())
        juros = float(input())
        meses = int(input())

        divida_juros_simples = (emprestimo * juros * meses) + emprestimo
        divida_juros_compostos = emprestimo * (1 + juros) ** meses

        print(f'DIFERENCA DE VALOR = {abs(divida_juros_simples - divida_juros_compostos) :.2f}')
        print(f'JUROS SIMPLES = {abs(divida_juros_simples - emprestimo) :.2f}')
        print(f'JUROS COMPOSTO = {abs(divida_juros_compostos - emprestimo) :.2f}')

    except EOFError:
        break
