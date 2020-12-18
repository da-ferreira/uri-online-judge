
e, d = map(int, input().split())

if e > d or d >= 24:
    print('Eu odeio a professora!')

elif e + 3 <= d:
    print('Muito bem! Apresenta antes do Natal!')
else:
    print('Parece o trabalho do meu filho!')

    if e + 2 <= 23:
        print('TCC Apresentado!')
    else:
        print('Fail! Entao eh nataaaaal!') 
