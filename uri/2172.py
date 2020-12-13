
while True:
    xp, monstro = map(int, input().split())
    if xp == 0 and monstro == 0:
        break

    print(monstro * xp)
