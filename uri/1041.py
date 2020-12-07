
pontos = input().split(' ')

x = float(pontos[0])
y = float(pontos[1])

if (x > 0) and (y > 0):  # <- Q1
	print('Q1')
if (x < 0) and (y > 0):  # <- Q2
	print('Q2')
if (x < 0) and (y < 0):  # <- Q3
	print('Q3')
if (x > 0) and (y < 0):  # <- Q4
	print('Q4')

if (x == 0) and (y == 0):  # <- Origem
	print('Origem')

if (x != 0) and (y == 0):  # <- Eixo X
	print('Eixo X')
if (x == 0) and (y != 0):  # <- Eixo Y
	print('Eixo Y')
