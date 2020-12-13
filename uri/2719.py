
casos = int(input())

for i in range(casos):
    n, peso_maximo = map(int, input().split())
    presentes = list(map(int, input().split()))

    viagens = 1
    temp = presentes[0]

    for j in range(1, n):
        if temp + presentes[j] <= peso_maximo:
            temp += presentes[j]
        else:
            viagens += 1
            temp = presentes[j]
    
    print(viagens)
