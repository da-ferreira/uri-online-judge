
criancas = []

while True:
    try:
        criancas.append(input())
    except EOFError:
        break

criancas.sort(key=str.casefold, reverse=True)
print(criancas[0])
