
def repetido(numero):
    numero = str(numero)
    
    if len(set(numero)) == len(numero):
        return True
    else:
        return False


while True:
    try:
        n, m = map(int, input().split())
        quantidade = 0

        for i in range(n, m+1):
            if repetido(i):
                quantidade += 1
        print(quantidade)
    except EOFError:
        break
