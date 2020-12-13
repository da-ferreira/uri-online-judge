
quantidade = int(input())

jogos = ''

for i in range(quantidade):
    a = input()
    jogos += a

jogos = jogos.replace('1', '')
print(len(jogos))
    