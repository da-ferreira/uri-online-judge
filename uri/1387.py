
while True:
	filhos = input().split(' ')
	homem = int(filhos[0])
	mulher = int(filhos[1])
	if homem == 0 and mulher == 0:
		break
	total = homem + mulher
	print(total)
