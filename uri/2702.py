
refeicoes_disponiveis = list(map(int, input().split()))
refeicoes_requisitadas = list(map(int, input().split()))

passageiros = 0

for i in range(3):
    if refeicoes_requisitadas[i] > refeicoes_disponiveis[i]:
        passageiros += (refeicoes_requisitadas[i] - refeicoes_disponiveis[i])
print(passageiros)
