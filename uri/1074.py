
casos = int(input())

for i in range(casos):
	num = int(input())
	
	if num % 2 == 0 and num > 0:  # <- Par positivo.
		print('EVEN POSITIVE')

	if num % 2 == 0 and num < 0:  # <- Par negativo.
		print('EVEN NEGATIVE')

	if num % 2 == 1 and num > 0:  # <- Ímpar positivo.
		print('ODD POSITIVE')

	if num % 2 == 1 and num < 0:  # <- Ímpar negativo.
		print('ODD NEGATIVE')

	if num == 0:
		print('NULL')
