
i = 1
j = 7
conta = 0
while True:
	print('I={} J={}'.format(i, j))
	j -= 1
	if j == 4:
		j = 7
		i += 2
		conta += 1
	if conta == 5:
		break
