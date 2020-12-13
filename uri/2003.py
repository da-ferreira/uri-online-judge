
def minutos(tempo):
    tempo = tempo.split(':')
    horas = int(tempo[0]) * 60
    return int(tempo[1]) + horas


while True:
    try:
        horario = input()
        temp = int(horario.replace(':', ''))

        if (temp + 60) > 760:
            chegada = minutos(horario)
            
            if chegada - 480 > 0:
                result = (chegada - 480) + 60
            else:
                result = 60 - (480 - chegada)

            print('Atraso maximo: {}'.format(result))
        else:
            print('Atraso maximo: 0')
    except:
        break




