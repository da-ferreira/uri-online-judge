
j = 1
while True:
    n = int(input())
    if n == 0:
        break

    nome_jogador1 = input()
    nome_jogador2 = input()

    print(f'Teste {j}')
    for i in range(n):
        num1, num2 = map(int, input().split())

        if (num1 + num2) % 2 == 0:
            print(nome_jogador1)
        else:
            print(nome_jogador2)
    
    print()
    j += 1
