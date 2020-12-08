
from math import gcd

casos = int(input())

for i in range(casos):
    par1 = input()
    par2 = input()

    par1 = int(par1, 2)
    par2 = int(par2, 2)

    if gcd(par1, par2) != 1:
        print(f'Pair #{i + 1}: All you need is love!') 
    else:
        print(f'Pair #{i + 1}: Love is not all you need!')
