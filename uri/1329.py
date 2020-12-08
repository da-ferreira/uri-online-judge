
while True:
    partidas = int(input())
    if partidas == 0:
        break

    jogos = input()
    print('Mary won {} times and John won {} times'.format(jogos.count('0'), jogos.count('1')))
