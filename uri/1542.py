
while True:
    entrada = input().split()
    if entrada[0] == '0':
        break

    q = int(entrada[0])
    d = int(entrada[1])
    p = int(entrada[2])

    paginas = (q * d * p) // (p - q)
    
    if paginas == 1:
        print(f'{paginas} pagina')
    else:
        print(f'{paginas} paginas')
