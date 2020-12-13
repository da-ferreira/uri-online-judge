
while True:
    try:
        tamanho, utilizado, warning, critical = map(int, input().split())
        porcentagem = utilizado / tamanho * 100

        if porcentagem >= critical:
            print('critical')
        elif porcentagem >= warning:
            print('warning')
        else:
            print('OK')
    except EOFError:
        break
