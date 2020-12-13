
minutos = int(input())
presente1, presente2 = map(int, input().split())

if (presente1 + presente2) <= minutos:
    print('Farei hoje!')
else:
    print('Deixa para amanha!')
