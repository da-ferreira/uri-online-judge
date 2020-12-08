
from string import ascii_uppercase
alfa = list(ascii_uppercase)

casos = int(input())

for i in range(casos):
    string = list(input())
    num = int(input())

    for j in range(len(string)):
        string[j] = alfa[alfa.index(string[j]) - num]
    
    print(''.join(string))
