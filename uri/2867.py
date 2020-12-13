
casos = int(input())

for i in range(casos):
    n, m  = map(int, input().split())
    resultado = n ** m
    print(len(str(resultado)))
