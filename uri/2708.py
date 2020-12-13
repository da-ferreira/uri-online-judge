
turistas = jipes = 0

while True:
    entrada = input().split()
    if entrada[0] == 'ABEND':
        break

    if entrada[0] == 'SALIDA':
        turistas += int(entrada[1])
        jipes += 1
    else:
        turistas -= int(entrada[1])
        jipes -= 1

print(turistas)
print(jipes)
