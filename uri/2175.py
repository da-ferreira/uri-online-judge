
tempo = list(map(float, input().split()))

nomes = {
    tempo[0]: 'Otavio',
    tempo[1]: 'Bruno',
    tempo[2]: 'Ian'
}

if tempo.count(min(tempo)) > 1:
    print('Empate')
else:
    print(nomes[min(tempo)])
