
qtd_alunos, qtd_minima = map(int, input().split())
horario_chegada = input()
horario_chegada += ' '

if (horario_chegada.count('-') + horario_chegada.count('0 ')) >= qtd_minima:
    print('YES')
else:
    print('NO')
