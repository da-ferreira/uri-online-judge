
while True:
    try:
        n, k = map(int, input().split())

        numeros = []

        while len(numeros) != n:
            temp = list(map(int, input().split())) 
            numeros += temp

        numeros.sort()

        k = n - k
        soma = sum(numeros[-1:k-1:-1])

        print(soma % 1000000007)
    except EOFError:
        break
