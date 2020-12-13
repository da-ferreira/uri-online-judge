
from string import ascii_uppercase

n = int(input())

for i in range(n):
    m = int(input())
    sequencia = input()

    swaps = 0

    for j in range(m):
       if sequencia[j] != ascii_uppercase[j]:
           swaps += 1

    if swaps == 2:
        print('There are the chance.')
    else:
        print("There aren't the chance.")
    