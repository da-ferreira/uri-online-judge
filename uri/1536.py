
casos = int(input())

tabela = {
    'pontos_time1': 0,
    'pontos_time2': 0,
    
    'saldo_time1': 0,
    'saldo_time2': 0,

    'gols_fora_de_casa_time1': 0,
    'gols_fora_de_casa_time2': 0
}

for i in range(casos):
    for j in range(2):
        entrada = input().split()

        time1 = int(entrada[0])  
        time2 = int(entrada[2])

        if j == 0:
            if time1 > time2:
                tabela['pontos_time1'] += 3
            elif time2 > time1:
                tabela['pontos_time2'] += 3
            else:
                tabela['pontos_time1'] += 1
                tabela['pontos_time2'] += 1

            tabela['saldo_time1'] += (time1 - time2)
            tabela['saldo_time2'] += (time2 - time1)

            tabela['gols_fora_de_casa_time2'] += time2
        else:
            if time1 > time2:
                tabela['pontos_time2'] += 3
            elif time2 > time1:
                tabela['pontos_time1'] += 3
            else:
                tabela['pontos_time1'] += 1
                tabela['pontos_time2'] += 1

            tabela['saldo_time1'] += (time2 - time1)
            tabela['saldo_time2'] += (time1 - time2)

            tabela['gols_fora_de_casa_time1'] += time2

    if tabela['pontos_time1'] > tabela['pontos_time2']:
        print('Time 1')
    elif tabela['pontos_time1'] < tabela['pontos_time2']:
        print('Time 2')
    else:
        if tabela['saldo_time1'] > tabela['saldo_time2']:
            print('Time 1')
        elif tabela['saldo_time1'] < tabela['saldo_time2']:
            print('Time 2')
        else:
            if tabela['gols_fora_de_casa_time1'] > tabela['gols_fora_de_casa_time2']:
                print('Time 1')
            elif tabela['gols_fora_de_casa_time1'] < tabela['gols_fora_de_casa_time2']:
                print('Time 2')
            else:
                print('Penaltis')

    for x in tabela:
        tabela[x] = 0
