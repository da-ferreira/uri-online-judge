
assassinos = {}
mortos = set()

while True:
    try:
        matou, morreu = input().split()

        if matou not in mortos:
            if matou not in assassinos:
                assassinos[matou] = 1
            else:
                assassinos[matou] += 1

        if morreu not in mortos:
            mortos.add(morreu)

        if morreu in assassinos:
            del assassinos[morreu]
    except EOFError:
        break

print('HALL OF MURDERERS')

for i in sorted(assassinos):
    print(i, assassinos[i])
