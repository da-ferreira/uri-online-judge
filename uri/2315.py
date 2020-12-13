
mes = [
    0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
]

dia1, mes1 = map(int, input().split())
dia2, mes2 = map(int, input().split())

dias = 0

if mes1 == mes2:
    print(dia2 - dia1)
else:
    for i in range(mes1, mes2+1):
        if i == mes1:
            dias += (mes[mes1] - dia1)
        elif i == mes2:
            dias += dia2
        else:
            dias += mes[i] 
    print(dias)
