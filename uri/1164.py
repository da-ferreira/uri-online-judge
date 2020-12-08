
vezes = int(input())
soma = 0

for i in range(vezes):
	num = int(input())
	for j in range(1, num):
		if num % j == 0:
			soma += j
		
	if soma == num:
		print('{} eh perfeito'.format(num))
	else:
		print('{} nao eh perfeito'.format(num))
	soma = 0
