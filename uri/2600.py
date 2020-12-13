
casos = int(input())

for i in range(casos):
    cima = int(input())
    meio = list(map(int, input().split()))
    baixo = int(input())

    dado = [cima] + meio + [baixo]

    if all(x in dado for x in range(1, 7)):
        if (dado[0] + dado[-1] == 7) and (dado[1] + dado[3] == 7) and (dado[2] + dado[4] == 7):
            print('SIM')
        else:
            print('NAO')
    else:
        print('NAO')
