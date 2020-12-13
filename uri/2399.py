
n = int(input())

campo_minado = []
minas = [0] * n

for i in range(n):
    campo_minado.append(int(input()))

for i in range(n):
    if i == 0:
        if n > 1 and campo_minado[0] == 1 and campo_minado[1] == 1:
            minas[0] = 2
        elif n > 1 and campo_minado[0] == 1 and campo_minado[1] == 0 or \
            n > 1 and campo_minado[0] == 0 and campo_minado[1] == 1:
            minas[0] = 1
        else:
            minas[0] = 0
    
    elif i == n - 1:
        if n > 1 and campo_minado[-1] == 1 and campo_minado[-2] == 1:
            minas[-1] = 2
        elif n > 1 and campo_minado[-1] == 1 and campo_minado[-2] == 0 or \
            n > 1 and campo_minado[-1] == 0 and campo_minado[-2] == 1:
            minas[-1] = 1
        else:
            minas[-1] = 0
    else:
        if campo_minado[i] == 1 and campo_minado[i + 1] == 1 and campo_minado[i - 1] == 1:
            minas[i] = 3
        
        elif campo_minado[i] == 0 and campo_minado[i + 1] == 1 and campo_minado[i - 1] == 1 or \
            campo_minado[i] == 1 and campo_minado[i + 1] == 0 and campo_minado[i - 1] == 1 or \
                campo_minado[i] == 1 and campo_minado[i + 1] == 1 and campo_minado[i - 1] == 0:
                minas[i] = 2
        
        elif campo_minado[i] == 1 and campo_minado[i + 1] == 0 and campo_minado[i - 1] == 0 or \
            campo_minado[i] == 0 and campo_minado[i + 1] == 0 and campo_minado[i - 1] == 1 or \
                campo_minado[i] == 0 and campo_minado[i + 1] == 1 and campo_minado[i - 1] == 0:
                minas[i] = 1
        else:
            minas[i] = 0

for i in minas:
    print(i)
