
n = int(input())

territorio = list(map(int, input().split()))

oeste = leste = 0

i = 0
j = n - 1

while i < j:
    if oeste < leste:
        oeste += territorio[i]
        i += 1
    elif leste < oeste:
        leste += territorio[j]
        j -= 1
    else:
        oeste += territorio[i]
        leste += territorio[j]
        j -= 1
        i += 1

if oeste < leste:
    i += 1

print(i)
