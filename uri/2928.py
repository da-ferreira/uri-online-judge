
quantidade = int(input())

eh_possivel = True
pulos = 0
temp = 0

for i in range(quantidade):
    caminho = input()

    if caminho[0] == '.':
        temp += 1
    else:
        if temp <= 2 and temp > 0:
            pulos += 1
        else:
            if temp >= 3:
                eh_possivel = False
        
        temp = 0

if temp > 0 and temp <= 2:
    pulos += 1  

if eh_possivel:
    print(pulos)
else:
    print('N')
