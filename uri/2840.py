
raio, gas = map(int, input().split())
volume = 4 * 3.1415 * ((raio ** 3) / 3)

print(round(gas // volume))
