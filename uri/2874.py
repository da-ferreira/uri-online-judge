
while True:
    try:
        n = int(input())
        frase = ''

        for i in range(n):
            binario = input()
            frase += chr(int(binario, 2))

        print(frase)
    except EOFError:
        break
