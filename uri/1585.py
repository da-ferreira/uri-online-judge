from math import floor

casos = int(input())

for i in range(casos):
    bambu1, bambu2 = map(int, input().split())
    print(f'{floor((bambu1 * bambu2) / 2)} cm2')
