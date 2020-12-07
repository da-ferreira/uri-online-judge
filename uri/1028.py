
from time import time

casos = int(input())

for i in range(casos):
    entrada = list(map(int, input().split()))

    inicio = time()    
    num1 = max(entrada)
    num2 = min(entrada)

    while num1 != 0 and num2 != 0:
        temp = num2

        num2 = num1 % num2
        num1 = temp

    if num1 != 0:
        print(num1)
    else:
        print(num2)
