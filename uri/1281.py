
casos = int(input())

disponiveis = {}
comprar = {}
total = 0
for i in range(casos):
    p_disponiveis = int(input())

    for j in range(p_disponiveis):
        temp = input()
        disponiveis[temp[0:temp.rfind(' ')]] = float(temp[temp.rfind(' '):])

    p_comprar = int(input())
    for j in range(p_comprar):
        temp2 = input()
        comprar[temp2[0:temp2.rfind(' ')]] = int(temp2[temp2.rfind(' '):])
    
    for key, valor in comprar.items():
        total += disponiveis[key] * valor
    
    print('R$ {:.2f}'.format(total))

    total = 0
    comprar.clear()
    disponiveis.clear()
