
i = 1
j = 7
temp = 0

for k in range(5):
	print('I={} J={}'.format(i, j))

	for q in range(2):
		temp = j
		j -= 1
		print('I={} J={}'.format(i, j))

	i += 2
	j = temp
	j += 3
