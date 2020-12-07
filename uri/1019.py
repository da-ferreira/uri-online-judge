
tempo_segundos = int(input())
conversao = list()

hora = tempo_segundos //  3600
conversao.insert(0, hora)
temporaria = tempo_segundos % 3600

minuto = temporaria // 60
conversao.insert(1, minuto)
temporaria %= 60

segundo = temporaria // 1
conversao.insert(2, segundo)

print('{}:{}:{}'.format(conversao[0], conversao[1], conversao[2]))
