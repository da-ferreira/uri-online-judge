
while True:
    try:
        alfabeto = input()
        lampadas = int(input())
        piscadas = list(map(int, input().split()))

        mensagem = ''

        for i in range(lampadas):
            mensagem += alfabeto[piscadas[i] - 1]
        print(mensagem)
    except EOFError:
        break
