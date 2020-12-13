
passaro, comida, quantidade = map(int, input().split())
vitorias_regias = list(map(int, input().split()))

folhas = 0

if (passaro + comida) > vitorias_regias[0]:
    temp = passaro + comida
    comida -= (temp - vitorias_regias[0])

for i in range(quantidade - 1):
    if (passaro + comida) > vitorias_regias[i + 1]:
        temp = passaro + comida

        comida -= (temp - vitorias_regias[i + 1])
        
        if comida >= 0:
            folhas += 1

        if comida < 0:            
            break
                
print(folhas)
