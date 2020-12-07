
gremio = inter = empate = 0
while True:
    grenal = input().split()

    if int(grenal[0]) > int(grenal[1]):
        inter += 1
    elif int(grenal[0]) < int(grenal[1]):
        gremio += 1
    else:
        empate += 1

    novo = int(input('Novo grenal (1-sim 2-nao)\n'))
    if novo == 2:
        break

print('{} grenais'.format(inter + gremio + empate))
print('Inter:{}'.format(inter))
print('Gremio:{}'.format(gremio))
print('Empates:{}'.format(empate))

if inter > gremio:
    print('Inter venceu mais')
elif inter < gremio:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')
