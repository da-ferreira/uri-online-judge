
while True:
    try:
        numero = int(input())
        multiplo = 1
        quantidade = 1

        while multiplo % numero != 0:
            multiplo = (10 * multiplo + 1) % numero
            quantidade += 1
        
        print(quantidade)
             
    except EOFError:
        break

