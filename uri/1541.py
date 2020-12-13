
from math import trunc, sqrt

while True:
    entrada = input().split()
    if len(entrada) == 1 and entrada[0] == '0':
        break

    a = int(entrada[0]); b = int(entrada[1]); c = int(entrada[2])

    print(trunc(sqrt(a * b * (100 / c))))
