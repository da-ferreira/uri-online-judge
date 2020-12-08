
while True:
    n = int(input())
    if n == 0:
        break

    incremento = 3
    sequencia = 1

    portas = [str(sequencia)]

    while (sequencia + incremento) <= n:
        portas.append(str(sequencia + incremento))
        sequencia += incremento
        incremento += 2
        

    print(' '.join(portas))
