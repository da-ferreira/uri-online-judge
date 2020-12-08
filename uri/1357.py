
number_to_braille = {
    1: '*.....',
    2: '*.*...',
    3: '**....',
    4: '**.*..',
    5: '*..*..',
    6: '***...',
    7: '****..',
    8: '*.**..',
    9: '.**...',
    0: '.***..'
}

braille_to_number = {
    '*.....': '1',
    '*.*...': '2',
    '**....': '3',
    '**.*..': '4',
    '*..*..': '5',
    '***...': '6',
    '****..': '7',
    '*.**..': '8',
    '.**...': '9',
    '.***..': '0'
}

while True:
    d = int(input())
    if d == 0:
        break

    operacao = input()
    
    if operacao == 'S':
        digitos = input()
        imprimir = []

        for i in range(d):
            imprimir.append(number_to_braille[int(digitos[i])])
        
        j = 0
        for i in range(3):
            for k in range(d):
                if k != d - 1:
                    print(imprimir[k][j:j + 2], end=' ')
                else:
                    print(imprimir[k][j:j + 2])

            j += 2 
    else:
        numeros = ['' for x in range(d)]

        for i in range(3):
            entrada = input().split()

            for j in range(d):
                numeros[j] += entrada[j]
        
        imprimir = ''

        for i in range(len(numeros)):
            imprimir += braille_to_number[numeros[i]]
        
        print(imprimir)
