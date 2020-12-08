
from math import factorial

while True:
    acm = input()
    if acm == '0':
        break
    
    decimal = 0
    j = 0
    for i in range(len(acm), 0, -1):
        decimal += int(acm[j]) * factorial(i)
        j += 1
    
    print(decimal)
