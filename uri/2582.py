testes = int(input())

musicas = {
    0: 'PROXYCITY',
    1: 'P.Y.N.G.',
    2: 'DNSUEY!',
    3: 'SERVERS',
    4: 'HOST!',
    5: 'CRIPTONIZE',
    6: 'OFFLINE DAY',
    7: 'SALT',
    8: 'ANSWER!',
    9: 'RAR?',
    10: 'WIFI ANTENNAS'
}

for i in range(testes):
    botoes = input().split(' ')
    botao1 = int(botoes[0])
    botao2 = int(botoes[1])

    song = botao1 + botao2
    print(musicas[song])
