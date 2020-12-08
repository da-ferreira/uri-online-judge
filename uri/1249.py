
lower = [
    '', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'
 ]

upper = [
    '', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'
 ]


while True:
    try:
        mensagem = input()
        codigo = ''

        for i in range(len(mensagem)):
            if mensagem[i].isalpha():
                if mensagem[i].islower():
                    codigo += lower[lower.index(mensagem[i]) + 13]
                else:
                    codigo += upper[upper.index(mensagem[i]) + 13]
            else:
                codigo += mensagem[i]
        print(codigo)
    except EOFError:
        break
