
casos = int(input())

for i in range(casos):
    texto = input().split()
    texto = sorted(texto, key=len, reverse=True)
    print(' '.join(texto))
