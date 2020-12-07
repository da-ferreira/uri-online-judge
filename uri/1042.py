
temporaria = input().split(' ')

valores = []
for i in range(3):
	valores.insert(i, int(temporaria[i]))

temporaria = valores[:]
valores.sort()

for i in valores:
	print(i)
print()

for i in temporaria:
	print(i)
