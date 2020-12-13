
casos = int(input())

for i in range(casos):
    mensagem = input()
    decodificada = []

    for j in mensagem:
        if j.islower():
            decodificada.append(j)
    
    decodificada.reverse()
    print(''.join(decodificada))
