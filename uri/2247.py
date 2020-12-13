
linha = 1
while True:
    n = int(input())
    if n == 0:
        break

    jao = ze = 0

    print(f'Teste {linha}')
    
    for i in range(n):
        joaozinho, zezinho = map(int, input().split())
        
        if i == 0:
            if joaozinho < zezinho:
                jao += (joaozinho - zezinho)
            else:
                ze += (zezinho - joaozinho)
            print(joaozinho - zezinho)

        else:
            joaozinho += jao
            jao = 0

            zezinho += ze
            ze = 0

            if joaozinho < zezinho:
                jao += (joaozinho - zezinho)
            else:            
                ze += (zezinho - joaozinho)

            print(joaozinho - zezinho)
    
    print()
    linha += 1
 