
casos = int(input())

for i in range(casos):
    joao = maria = 0

    for j in range(3):
        pontos, distancia = map(int, input().split())
        joao += (pontos * distancia)
    
    for j in range(3):
        pontos, distancia = map(int, input().split())
        maria += (pontos * distancia)
    
    if maria > joao:
        print('MARIA')
    else:
        print('JOAO')
