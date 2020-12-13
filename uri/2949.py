
pessoas = int(input())

hobbit = humano = elfo = anao = mago = 0

for i in range(pessoas):
    person = input().split()

    if person[1] == 'X':
        hobbit += 1
    elif person[1] == 'H':
        humano += 1 
    elif person[1] == 'E':
        elfo += 1
    elif person[1] == 'A':
        anao += 1
    else:
        mago += 1

print('{} Hobbit(s)'.format(hobbit))
print('{} Humano(s)'.format(humano))
print('{} Elfo(s)'.format(elfo))
print('{} Anao(s)'.format(anao))
print('{} Mago(s)'.format(mago))
