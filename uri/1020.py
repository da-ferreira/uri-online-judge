dias = int(input())

ano = dias // 365
temporaria = dias % 365

mes = temporaria // 30
temporaria = temporaria % 30

dia = temporaria // 1

print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(dia))
