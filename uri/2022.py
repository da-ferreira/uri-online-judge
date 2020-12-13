
while True:
    try:
        nome, tamanho_lista = input().split()
        presentes = []

        for i in range(int(tamanho_lista)):
            nome_presente = input()
            preco, preferencia = input().split()

            presentes.append([nome_presente, float(preco), int(preferencia)])
        
        presentes.sort(key=lambda k: k[0])
        presentes.sort(key=lambda k: k[1])
        presentes.sort(key=lambda k: k[2], reverse=True)

        print(f'Lista de {nome}')

        for i in range(int(tamanho_lista)):
            print(f'{presentes[i][0]} - R${presentes[i][1] :.2f}')
        
        print()
    except EOFError:
        break
