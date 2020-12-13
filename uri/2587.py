
casos = int(input())

for i in range(casos):
    tentativa1 = input()
    tentativa2 = input()
    palavra = input()

    temp = []

    for i in range(len(palavra)):
        if palavra[i] == '_':
            temp.append(i)
    
    if tentativa1[temp[0]] == tentativa2[temp[1]] or tentativa1[temp[1]] == tentativa2[temp[0]]:
        print('Y')
    else:
        print('N')
