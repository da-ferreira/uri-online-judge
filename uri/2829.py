
quantidade = int(input())
palavras = []

for i in range(quantidade):
    palavras.append(input())

palavras.sort()
palavras.sort(key=str.casefold)

for i in palavras:
    print(i)
