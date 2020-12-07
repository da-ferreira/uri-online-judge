
horas = input().split(' ')

inicio = int(horas[0])
fim = int(horas[1])

if inicio < fim:
	tempo = fim - inicio
else:
	tempo = (24 - inicio) + fim
print('O JOGO DUROU {} HORA(S)'.format(tempo))
