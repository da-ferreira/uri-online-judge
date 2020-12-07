
from datetime import timedelta

while True:
    hora = input().split()
    if (hora[0] == '0') and (hora[1] == '0') and (hora[2] == '0') and (hora[3] == '0'):
        break

    dormir = timedelta(hours=int(hora[0]), minutes=int(hora[1]))
    acordar = timedelta(hours=int(hora[2]), minutes=int(hora[3]))

    minutos = str(acordar - dormir).split()

    if len(minutos) == 3:
        del minutos[0:2]
        minutos = minutos[0]
        minutos = minutos.replace(':', ' ')
        minutos = minutos.split()

        soma = (int(minutos[0]) * 60) + int(minutos[1])
    else:
        minutos = minutos[0]
        minutos = minutos.replace(':', ' ')
        minutos = minutos.split()
        soma = (int(minutos[0]) * 60) + int(minutos[1])
    
    print(soma)
