
qtd_pecas = int(input())
pecas = list(map(int, input().split()))

for i in range(1, qtd_pecas + 1):
    if i not in pecas:
        print(i)
        break
