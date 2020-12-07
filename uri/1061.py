
from datetime import timedelta

dia_comeco = input().split()
inicio = input().split()
dia_fim = input().split()
fim = input().split()

evento_inicio = timedelta(days=int(dia_comeco[1]), hours=int(inicio[0]), minutes=int(inicio[2]), seconds=int(inicio[4]))
evento_fim = timedelta(days=int(dia_fim[1]), hours=int(fim[0]), minutes=int(fim[2]), seconds=int(fim[4]))

#print(evento_inicio, evento_fim) ###3

tempo = evento_fim - evento_inicio
dia = tempo.days

tempo = str(tempo).split()
if len(tempo) == 3:
    del tempo[0:2]

tempo = tempo[0].split(':')

hora = int(tempo[0])
minuto = int(tempo[1])
segundo = int(tempo[2])

if (dia == 0) and (hora == 0) and (minuto == 0) and (segundo <= 59):
    print('0 dia(s)')
    print('0 hora(s)')
    print('1 minuto(s)')
    print('0 segundo(s)')
else:
    print('{} dia(s)'.format(dia))
    print('{} hora(s)'.format(hora))
    print('{} minuto(s)'.format(minuto))
    print('{} segundo(s)'.format(segundo))
