
quantidade = int(input())
duendes = []

for i in range(quantidade):
    nome, idade = input().split()
    duendes.append([nome, int(idade)])

times = [[] for x in range(quantidade // 3)]

duendes.sort(key=lambda k: k[0])
duendes.sort(key=lambda k: k[1], reverse=True)

point = 0

while len(duendes) > 0:
    times[point].append(duendes.pop(0))

    if point == quantidade // 3 - 1:
        point = 0
    else:
        point += 1

for i in range(quantidade // 3):
    print(f'Time {i + 1}')

    for j in times[0]:
        print(j[0], j[1])
    
    print()
    times.pop(0)
    