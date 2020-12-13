
roupas = int(input())

minLavadora, maxLavadora = map(int, input().split())
minSecadora, maxSecadora = map(int, input().split())

if (roupas >= minLavadora and roupas <=maxLavadora) and (roupas >= minSecadora and roupas <= maxSecadora):
    print('possivel')
else:
    print('impossivel')
