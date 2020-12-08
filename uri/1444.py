
from math import ceil

while True:
    n = int(input())
    if n == 0:
        break

    if n != 1:
        temp = n / 3
        corridas = ceil(temp)

        while temp > 1:
            temp /= 3
            corridas += ceil(temp)

        print(corridas) 
    else:
        print(0)
    