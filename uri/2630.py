casos = int(input())

for i in range(1, casos+1):
    conversao = input()
    r, g, b = map(int, input().split())
    temp = [r, g, b]

    if conversao == 'eye':
        p = int((r * 0.3) + (g * 0.59) + (b * 0.11))
    elif conversao == 'mean':
        p = (r + g + b) // 3
    elif conversao == 'min':
        p = min(temp)
    else:
        p = max(temp)
    print(f'Caso #{i}: {p}')
