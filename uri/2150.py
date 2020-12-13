
while True:
    try:
        vogais = list(input())
        frase = input()
        quantidade = 0

        for i in range(len(vogais)):
            quantidade += frase.count(vogais[i])
        print(quantidade)
    except EOFError:
        break
