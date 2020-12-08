
quantidade = int(input())

for i in range(quantidade):
    mensagem = input().split()

    msg_oculta = ''
    for j in range(len(mensagem)):
        msg_oculta += mensagem[j][0]
    print(msg_oculta)
