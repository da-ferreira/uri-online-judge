
n, t = map(int, input().split())

times = [[] for x in range(t)]
jogadores = []

for i in range(n):
    entrada = input().split()
    jogadores.append([entrada[0], int(entrada[1])])

jogadores.sort(key=lambda k: k[1], reverse=True)

temp = 0

while len(jogadores) != 0:
    times[temp].append(jogadores[0][0])
    jogadores.pop(0)
    temp += 1

    if temp == t:
        temp = 0
    

for i in range(t):
    print(f'Time {i + 1}')

    for j in sorted(times[i]):
        print(j)
    
    print()
