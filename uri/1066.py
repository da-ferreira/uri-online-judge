
pares = impares = positivo = negativo = 0

for i in range(5):
	num = int(input())

	if num % 2 == 0:
		pares += 1
	if num % 2 == 1:
		impares += 1
	if num > 0:
		positivo += 1
	if num < 0:
		negativo += 1

print('{} valor(es) par(es)'.format(pares))
print('{} valor(es) impar(es)'.format(impares))
print('{} valor(es) positivo(s)'.format(positivo))
print('{} valor(es) negativo(s)'.format(negativo))
