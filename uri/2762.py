
valor = input()

novo = valor[valor.index('.')+1:]
novo += '.'
novo += valor[0:valor.index('.')]
print(float(novo))
