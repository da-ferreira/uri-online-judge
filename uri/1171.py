
vezes = int(input())
numeros = []
cada_numero = []

for i in range(vezes):
	num = int(input())
	
	if num not in cada_numero:
		cada_numero.append(num)

	numeros.append(num)

cada_numero.sort()

for j in range(len(cada_numero)):
	print('{} aparece {} vez(es)'.format(cada_numero[j], numeros.count(cada_numero[j])))
