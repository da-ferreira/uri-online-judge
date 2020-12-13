
quantidade = int(input())
nomes = [] 

for i in range(quantidade):
    nomes.append(input())

nomes.sort(key=len)
temp = []

while len(nomes) != 0:
    i = 0

    while i < len(nomes):
        if len(temp) == 0:
            temp.append(nomes[i])
            nomes.pop(0)
        else:
            if len(nomes[i]) > len(temp[-1]):
                temp.append(nomes[i])
                nomes.pop(i)
            else:
                i += 1

    print(', '.join(temp))
    temp = []
