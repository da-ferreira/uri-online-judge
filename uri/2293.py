
linhas, colunas = map(int, input().split())

terreno = []
maior = 0

for i in range(linhas):
    terreno.append(list(map(int, input().split())))

    if sum(terreno[-1]) > maior:
        maior = sum(terreno[-1])

temp = [] 

for i in range(colunas):
    for j in range(linhas):
        temp.append(terreno[j][i])

    if sum(temp) > maior:
        maior = sum(temp)
    
    temp = []

print(maior)
