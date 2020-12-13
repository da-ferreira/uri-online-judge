
def valor_golpe(bonus, ataque, defesa, treinador):
    if treinador % 2 == 0:
        return ((ataque + defesa) / 2) + bonus
    else:
        return (ataque + defesa) / 2

instancias = int(input())

for i in range(instancias):
    valor_bonus = int(input())
    dabriel = list(map(int, input().split()))
    guarte = list(map(int, input().split()))

    dabriel = valor_golpe(valor_bonus, dabriel[0], dabriel[1], dabriel[2])
    guarte = valor_golpe(valor_bonus, guarte[0], guarte[1], guarte[2])

    if dabriel > guarte:
        print('Dabriel')
    elif guarte > dabriel:
        print('Guarte')
    else:
        print('Empate')
