
vezes = int(input())
maiuscula = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(vezes):
	jogo = input()
	
	num1 = int(jogo[0])
	letra = jogo[1]
	num2 = int(jogo[2])

	if letra in maiuscula and num1 != num2:
			print(num2 - num1)
	if num1 == num2:
		print(num1 * num2)
	if letra not in maiuscula and num1 != num2:
		print(num2 + num1)
