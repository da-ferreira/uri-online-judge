
n, m = map(int, input().split())
fechadura = list(map(int, input().split()))

i = 0
movimentos = 0

while i < n - 1:
    if fechadura[i] < m:

        while fechadura[i] < m:
            fechadura[i] += 1
            fechadura[i + 1] += 1

            movimentos += 1
        
        i += 1

    elif fechadura[i] > m:
        while fechadura[i] > m:
            fechadura[i] -= 1
            fechadura[i + 1] -= 1

            movimentos += 1

        i += 1
    else:
        i += 1

print(movimentos)

