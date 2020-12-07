
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break

    alice = set(map(int, input().split()))
    beatriz = set(map(int, input().split()))

    trocas = (len(alice - beatriz), len(beatriz - alice))
    print(min(trocas))
