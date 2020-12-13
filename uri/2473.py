
numeros_aposta = list(map(int, input().split()))
numeros_sorteio = list(map(int, input().split()))

acertos = 0

for i in range(6):
    if numeros_aposta[i] in numeros_sorteio:
        acertos += 1

if acertos == 3:
    print('terno')
elif acertos == 4:
    print('quadra')
elif acertos == 5:
    print('quina')
elif acertos == 6:
    print('sena')
else:
    print('azar')
