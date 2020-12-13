
def shoelace_formula(vertices):
    soma1 = 0
    soma2 = 0

    for i in range(len(vertices) - 1):
        soma1 += vertices[i][0] * vertices[i + 1][1]
        soma2 += vertices[i][1] * vertices[i + 1][0]
    
    soma1 += vertices[-1][0] * vertices[0][1]
    soma2 += vertices[-1][1] * vertices[0][0]

    area = abs(soma1 - soma2)
    area = area / 2

    return area


casos = int(input())

for i in range(casos):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    area = shoelace_formula([[x1, y1], [x2, y2], [x3, y3]])

    print(f'{area :.3f}')
