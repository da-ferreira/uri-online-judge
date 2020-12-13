
n = int(input())
candidatos = list(map(int, input().split()))

if max(candidatos) >= (45 / 100 * sum(candidatos)):
    print(1)
else:
    if max(candidatos) >= (40 / 100 * sum(candidatos)):
        dez_porcento = 10 / 100 * sum(candidatos)
        maior = max(candidatos)
        
        candidatos.remove(maior)
        
        verify = 0

        for i in range(len(candidatos)):
            if (maior - dez_porcento) >= candidatos[i]:
                verify += 1  
        
        if verify == len(candidatos):
            print(1)
        else:
            print(2)
    else:
        print(2)
