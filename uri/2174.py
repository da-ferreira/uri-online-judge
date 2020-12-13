
pokemons = int(input())
capturados = set()

for i in range(pokemons):
    capturados.add(input())

print('Falta(m) {} pomekon(s).'.format(151 - len(capturados)))
