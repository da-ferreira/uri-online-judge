
dentro = fora = 0

vezes = int(input())

for i in range(vezes):
	num = int(input())

	if num >= 10 and num <= 20:
		dentro += 1
	else:
		fora += 1

print('{} in'.format(dentro))
print('{} out'.format(fora))
