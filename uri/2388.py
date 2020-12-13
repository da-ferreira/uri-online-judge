
intervalos = int(input())
distancia_km = 0

for i in range(intervalos):
    tempo, velocidade = map(int, input().split())
    distancia_km += (tempo * velocidade)

print(distancia_km)
