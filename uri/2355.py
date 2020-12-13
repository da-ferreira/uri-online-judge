
from math import floor, ceil

while True:
    tempo = int(input())
    if tempo == 0:
        break

    print(f'Brasil {floor(tempo / 90)} x Alemanha {ceil(tempo / 12.857142857142858)}')
