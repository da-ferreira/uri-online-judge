
equipes = 'ABCDEFGHIJKLMNOP'
finalistas = []

for i in range(0, 16, 2):
    time1, time2 = map(int, input().split())
    
    if time1 > time2:
        finalistas.append(equipes[i])
    else:
        finalistas.append(equipes[i+1])

equipes = ''.join(finalistas)
finalistas.clear()

for i in range(0, 8, 2):
    time1, time2 = map(int, input().split())

    if time1 > time2:
        finalistas.append(equipes[i])
    else:
        finalistas.append(equipes[i+1])

equipes = ''.join(finalistas)
finalistas.clear()

for i in range(0, 4, 2):
    time1, time2 = map(int, input().split())

    if time1 > time2:
        finalistas.append(equipes[i])
    else:
        finalistas.append(equipes[i+1])

time1, time2 = map(int, input().split())

if time1 > time2:
    print(finalistas[0])
else:
    print(finalistas[1])       
