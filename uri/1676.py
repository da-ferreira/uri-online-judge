
liberados = [2]

n = [x for x in range(2, 34000 + 1)]

i = 2

while len(liberados) < 3000:
    if i == 2:
        n.pop(0)

        j = 1
        while j < len(n):
            n.pop(j)
            j += 1    


        i = n[0]
        liberados.append(n.pop(0))
    else:
        j = i - 1

        while j < len(n):
            n.pop(j)
            j += (i - 1)
        
        i = n[0]
        liberados.append(n.pop(0))


while True:
    termo = int(input())
    if termo == 0:
        break

    print(liberados[termo - 1])
