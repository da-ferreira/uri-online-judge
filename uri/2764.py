
data = input()

dia = data[0:2]
mes = data[3:5]
ano = data[6:]

print('{}/{}/{}'.format(mes, dia, ano))
print('{}/{}/{}'.format(ano, mes, dia))
print('{}-{}-{}'.format(dia, mes, ano))
