
while True:
    try:
        hora, minuto = map(int, input().split())

        hora = str(hora // 30)
        minuto = str(minuto // 6)

        if len(hora) == 1:
            hora = f'0{hora}'
        if len(minuto) == 1:
            minuto = f'0{minuto}'

        print(f'{hora}:{minuto}')
    except EOFError:
        break
