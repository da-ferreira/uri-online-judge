
valores = []
for i in range(6):
	num = float(input())
	if num > 0:
		valores.append(num)

print('{} valores positivos'.format(len(valores)))
print('{:.1f}'.format(sum(valores) / len(valores)))
