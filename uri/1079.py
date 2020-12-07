
casos = int(input())

for i in range(casos):
	valores = input().split()
	primeiro = float(valores[0]) * 2
	segundo = float(valores[1]) * 3
	terceiro = float(valores[2]) * 5

	media = (primeiro + segundo + terceiro) / 10
	print('{:.1f}'.format(media))
