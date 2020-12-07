
lista = []
lista.append(int(input()))
lista.append(int(input()))
lista.sort()

x = lista[0]
y = lista[1]

for i in range(x+1, y):
	if (i % 5 == 2) or (i % 5 == 3):
		print(i)
