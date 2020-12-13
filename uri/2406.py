
casos = int(input())

for i in range(casos):
    expressao = input()

    pilha = []

    for caracter in expressao:
        if caracter == '(':
            pilha.append('(')

        elif caracter == '[':
            pilha.append('[')

        elif caracter == '{':
            pilha.append('{')
        
        elif caracter == ')' and len(pilha) > 0 and pilha[-1] == '(':
            pilha.pop()

        elif caracter == ')':
            pilha.append(')')

        elif caracter == ']' and len(pilha) > 0 and pilha[-1] == '[':
            pilha.pop()

        elif caracter == ']':
            pilha.append(']')

        elif caracter == '}' and len(pilha) > 0 and pilha[-1] == '{':
            pilha.pop()
        
        elif caracter == '}':
            pilha.append('}')

    if len(pilha) == 0:
        print('S')
    else:
        print('N')
    