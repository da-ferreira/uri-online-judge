
lados = int(input())

if lados < 4:
    print(0)
else:
    quantidade = 2; lados -= 4
    j = 2
    for i in range(lados):
        quantidade += (j + 1) 
        j += 1
    print(quantidade)
    