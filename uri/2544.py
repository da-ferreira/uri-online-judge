
from math import log2

while True:
    try:
        numero = int(input())
        
        print(int(log2(numero)))
    except EOFError:
        break
