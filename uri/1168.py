
led = {0: 6, 1: 2, 2: 5, 3: 5,
       4: 4, 5: 5, 6: 6, 7: 3,
       8: 7, 9: 6}

testes = int(input())
leds = 0

for i in range(testes):
    numero = input()
    for j in numero:
        leds += led[int(j)]
    print('{} leds'.format(leds))
    
    leds = 0
