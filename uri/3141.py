nome = input()

dia_atual, mes_atual, ano_atual = map(int, input().split('/'))
dia_nascimento, mes_nascimento, ano_nascimento = map(int, input().split('/'))

if (mes_atual < mes_nascimento) or ((dia_atual < dia_nascimento) and (mes_atual == mes_nascimento)):
    ano_nascimento += 1

if dia_atual == dia_nascimento and mes_atual == mes_nascimento:
    print('Feliz aniversario!')

print(f'Voce tem {ano_atual - ano_nascimento} anos {nome}.')
