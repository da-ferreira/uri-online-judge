
c_testes = int(input())

for i in range(c_testes):
    escolha = input().split()
    
    jogador1 = escolha[0:2]
    jogador2 = escolha[2:]

    numeros = list(map(int, input().split()))
    numeros = sum(numeros)

    if (jogador1[1] == 'PAR' and numeros % 2 == 0) or (jogador1[1] == 'IMPAR' and numeros % 2 == 1):
        print(jogador1[0])
    elif (jogador2[1] == 'PAR' and numeros % 2 == 0) or (jogador2[1] == 'IMPAR' and numeros % 2 == 1):
        print(jogador2[0])
