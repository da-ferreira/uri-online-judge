
quantidade = int(input())
valores = input().split()

maior = 0
v = 1
for i in range(0, quantidade - 1):
    if valores[i] == valores[i+1]:
        v += 1
    else:
        if v > maior:
            maior = v
        v = 1

if v > maior:
    print(v)
else:   
    print(maior)
