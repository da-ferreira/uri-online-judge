
from datetime import timedelta

hora = input().split()

saida = timedelta(hours=int(hora[0]))
tempo_viagem = timedelta(hours=int(hora[1]))
fuso = timedelta(hours=int(hora[2]))

horario = str((saida + tempo_viagem) + fuso).split()

if len(horario) == 3:
    del horario[0:2]
    horario = horario[0]
    horario = horario.replace(':', ' ')
    horario = horario.split()
    hora_local = int(horario[0])
else:
    horario = horario[0]
    horario = horario.replace(':', ' ')
    horario = horario.split()
    hora_local = int(horario[0])
print(hora_local)
