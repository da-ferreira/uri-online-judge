
quantidade, muralha = map(int, input().split())

for i in range(quantidade):
    titan = input().split()
    altura = int(titan.pop())

    if altura > muralha:
        print(' '.join(titan))

