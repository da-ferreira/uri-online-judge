
from itertools import permutations

casos = int(input())

for i in range(casos):
    string = input()
    permutacoes = list(set(permutations(string, len(string))))
    permutacoes.sort()

    for j in permutacoes:
        print(''.join(j))
    
    print()
