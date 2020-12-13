
quantidade, capacidade = map(int, input().split())

soma = 0
excedeu = False

for i in range(quantidade):
    sairam, entraram = map(int, input().split())
    
    soma -= sairam
    soma += entraram

    if soma > capacidade:
        excedeu = True
        
if excedeu:
    print('S')
else:
    print('N')
