
casos = 1

while True:
    try:
        n = int(input())
        senha = ''

        teclas = list(map(float, input().split()))
        temp = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        teclas = [[teclas[x], temp[x]] for x in range(10)]
        teclas.sort(key=lambda k: k[0], reverse=True)

        for i in range(n):
            senha += teclas[i][1]
        
        print(f'Caso {casos}: {senha}')
        casos += 1
    except EOFError:
        break
