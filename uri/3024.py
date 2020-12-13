
quantidade, maximo = map(int, input().split())
montanhas = list(map(int, input().split()))

temp = mirantes = 1

for i in range(1, quantidade):
    if (montanhas[i] - montanhas[i - 1]) <= maximo:
        temp += 1
    else:
        if temp > mirantes:
            mirantes = temp
        
        temp = 1

if temp > mirantes:
    mirantes = temp

print(mirantes)
