
quantidade = int(input())
pessoas = {}

for i in range(quantidade):
    entrada = input().split()
    nome = entrada.pop(0)

    pessoas[nome] = set(entrada)
    
while True:
    try:
        nome_consulta, presente = input().split()

        if nome_consulta in pessoas and presente in pessoas[nome_consulta]:
            print('Uhul! Seu amigo secreto vai adorar o/')
        else:
            print('Tente Novamente!')    
    except EOFError:
        break
