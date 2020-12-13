
n = int(input())
tempo = 10
ultimas = []

for i in range(n):
    ultimas.append(int(input()))

    if len(ultimas) == 2:
        if ultimas[1] - ultimas[0] <= 10:
            tempo += ultimas[1] - ultimas[0]
        else:
            tempo += 10

        ultimas.pop(0)

print(tempo)
