
while True:
    try:
        expressao = input()
        pilha = []
        temp = False
        
        for caracter in expressao:
            if caracter == '(':
                pilha.append(caracter)
            elif caracter == ')' and len(pilha) == 0:
                temp = True
                break
            elif caracter == ')' and len(pilha) > 0:
                pilha.remove('(')

        if temp or len(pilha) > 0:
            print('incorrect')
        else:
            print('correct')
    except EOFError:
        break
        