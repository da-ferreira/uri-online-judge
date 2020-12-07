
valor = []
valor.append(int(input()))
valor.append(int(input()))
valor.sort()

x = valor[0]
y = valor[1]

soma = 0
for i in range(x+1, y):
	if i % 2 == 1:
		soma += i
print(soma)
