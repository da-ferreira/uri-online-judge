
while True:
    try:
        jogadores = int(input())
        votos = list(map(int, input().split()))

        if votos.count(1) >= ((jogadores / 3) * 2):
            print('impeachment')
        else:
            print('acusacao arquivada')
    except EOFError:
        break
