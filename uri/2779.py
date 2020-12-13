
total_figurinhas = int(input())
compradas = int(input())

figurinhas = set()

for i in range(compradas):
    figurinhas.add(int(input()))

print(total_figurinhas - len(figurinhas))
