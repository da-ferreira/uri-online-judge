
renas = [
    'Dasher', 'Dancer', 'Prancer', 'Vixen', 'Comet', 'Cupid', 'Donner', 'Blitzen', 'Rudolph'
]

bolas_de_neves = sum(list(map(int, input().split())))

j = 0
for i in range(bolas_de_neves):
    vencedora = renas[j]
    j += 1

    if j == 9:
        j = 0

print(vencedora)
