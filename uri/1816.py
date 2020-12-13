
from string import ascii_uppercase

instancias = 1

while True:
    m = int(input())
    if m == 0:
        break

    codificado = list(map(int, input().split()))
    alfabeto = list(ascii_uppercase)
    mensagem = ''

    for i in range(m):
        mensagem += alfabeto[codificado[i] - 1]
        alfabeto.insert(0, alfabeto.pop(codificado[i] - 1))
    
    print(f'Instancia {instancias}')
    print(mensagem)
    print()

    instancias += 1
