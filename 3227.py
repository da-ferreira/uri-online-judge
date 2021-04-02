
diferenca = int(input())
fila = list(input())

homem = mulher = 0
boate = ''

for i in range(len(fila)):
    if abs(homem - mulher) < diferenca:
        boate += fila.pop(0)

        if boate[-1] == 'W':
            mulher += 1
        else:
            homem += 1

    else:
        if homem > mulher:
            if len(fila) > 1 and fila[1] == 'W':
                boate += fila.pop(1)
                mulher += 1

            elif len(fila) > 0 and fila[0] == 'W':
                boate += fila.pop(0)
                mulher += 1
            else:
                break
        else:
            if len(fila) > 1 and fila[1] == 'M':
                boate += fila.pop(1)
                homem += 1
            elif len(fila) > 0 and fila[0] == 'M':
                boate += fila.pop(0)
                homem += 1
            else:
                break

print(len(boate))
    
