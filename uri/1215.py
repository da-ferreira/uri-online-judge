
from string import ascii_lowercase

palavras = set()

while True:
    try:
        linhas = input()

        temp = ''
        for i in linhas:
            if i.casefold() in ascii_lowercase and i != ' ':
                temp += i.casefold()
            else:
                if temp != '':
                    palavras.add(temp)
                temp = ''
        
        if len(temp) > 0:
            palavras.add(temp)
            temp = ''
    except EOFError:
        break

for i in sorted(palavras):
    print(i)
