
while True:
    try:
        frase = list(input())
        nova_frase = []
        
        for i in range(len(frase)):
            if frase[i] != ',' and frase[i] != '.':
                nova_frase.append(frase[i])
            else:
                if frase[i - 1] == ' ':
                    nova_frase.pop()
                    nova_frase.append(frase[i])
                else:
                    nova_frase.append(frase[i])

        print(''.join(nova_frase))
    except EOFError:
        break
