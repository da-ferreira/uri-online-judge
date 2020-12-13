
l, n = map(int, input().split())

irregulares = {}
palavras = []

consoantes = ['b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', ' s', 't', 'v', 'w', 'x', 'z']

for i in range(l):
    singular, plural = input().split()
    irregulares[singular] = plural

for i in range(n):
    word = input()

    if word in irregulares:
        palavras.append(irregulares[word])
    else:
        if word[-2] in consoantes and word[-1] == 'y':
            palavras.append(word[0:-1] + 'ies')
        
        elif word.endswith('o') or word.endswith('s') or word.endswith('ch') or \
            word.endswith('sh') or word.endswith('x'):
            palavras.append(word + 'es')
        else:
            palavras.append(word + 's')

for word in palavras:
    print(word)
