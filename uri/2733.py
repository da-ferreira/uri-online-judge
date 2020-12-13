
while True:
    try:
        quantidade = int(input())
        resultado = 0
        livros = []

        for i in range(quantidade):
            book = int(input())

            if book not in livros:
                resultado += 1

                if len(livros) < 4:
                    livros.append(book)
                else:
                    livros.pop(0)
                    livros.append(book)
        
        print(resultado)
    except EOFError:
        break
