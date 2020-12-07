
for i in range(100):
	num = int(input())
	
	if i == 0:
		maior = num
		indice = i+1
	else:
		if num > maior:
			maior = num
			indice = i+1

print(maior)
print(indice)
