
pulo_do_sapo, numero_canos = map(int, input().split())
pulos = list(map(int, input().split()))

veracidade = True

for i in range(len(pulos)-1):
    if pulos[i+1] > pulos[i]:
        if (pulos[i+1] - pulos[i]) > pulo_do_sapo:
            veracidade = False
            break
    else:
        if (pulos[i] - pulos[i+1]) > pulo_do_sapo:
            veracidade = False
            break

if veracidade:
    print('YOU WIN')
else:
    print('GAME OVER')
