
while True:
    qtd_atacantes, qtd_defensores = map(int, input().split())
    if qtd_atacantes == 0 and qtd_defensores == 0:
        break

    atacantes = list(map(int, input().split()))
    defensores = list(map(int, input().split()))

    empedido = 'N'

    defensores.sort()

    if min(atacantes) < defensores[1]:
        empedido = 'Y'

    print(empedido)
