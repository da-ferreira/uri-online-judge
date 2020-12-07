
hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

horas = hora_final - hora_inicial
minutos = minuto_final - minuto_inicial

if minutos < 0:
    minutos += 60
    horas -= 1

if horas < 0:
    horas += 24

if horas == 0 and minutos == 0:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')
