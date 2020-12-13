
qtd_interruptores, qtd_lampadas = map(int, input().split())

interruptores = {x: 0 for x in range(qtd_interruptores)}
lampadas = [False] * qtd_lampadas

acessas = list(map(int, input().split()))

for i in range(1, acessas[0] + 1):
    lampadas[acessas[i] - 1] = True 

condicao_de_parada = lampadas.copy()

for i in range(qtd_interruptores):
    entrada = list(map(int, input().split()))
    entrada.pop(0)

    interruptores[i] = entrada


i = 0
resultado = 0

while True:
    for j in interruptores[i]:
        if lampadas[j - 1]:
            lampadas[j - 1] = False
        else:
            lampadas[j - 1] = True
        
    resultado += 1

    if all(not x for x in lampadas):
        break


    if i == qtd_interruptores - 1:
        if lampadas == condicao_de_parada:
            resultado = -1
            break

        i = 0
    else:
        i += 1

print(resultado)
