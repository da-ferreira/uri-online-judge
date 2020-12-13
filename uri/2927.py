
alunos, computadores, queimados, sem_compilador = map(int, input().split())

computadores -= 1
computadores -= queimados
computadores -= sem_compilador

if computadores >= alunos:
    print('Igor feliz!')
else:
    if queimados > (sem_compilador / 2):
        print('Caio, a culpa eh sua!')
    else:
        print('Igor bolado!')
