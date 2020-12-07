
num = int(input())
k = 1  # <- Número que vai ser elevado ao quadrado e ao cubo.

for i in range(num):
	print('{} {} {}'.format(k, k ** 2, k ** 3))
	k += 1
	