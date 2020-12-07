
num = int(input())
k = 1  # Número principal da sequencia.

for i in range(num):
	for j in range(1):
		dobro = k * k
		triplo = k * dobro
		print('{} {} {}'.format(k, dobro, triplo))
		print('{} {} {}'.format(k, dobro+1, triplo+1))
	k += 1
