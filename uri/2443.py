
a, b, c, d = map(int, input().split())

if b == d:
    numerador = a + c
    denominador = b
else:
    denominador = b * d
    numerador = (denominador / b * a) + (denominador / d * c) 

menor = min([numerador, denominador])

if menor == denominador:
    while True:
        if numerador % menor == 0 and denominador % menor == 0:
            denominador /= menor
            numerador /= menor
            break
        else:
            menor -= 1
else:
    while True:
        if denominador % menor == 0 and numerador % menor == 0:
            numerador /= menor
            denominador /= menor   
            break
        else:
            menor -= 1

print(int(numerador), int(denominador))
