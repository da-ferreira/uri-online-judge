
while True:
    consultas = int(input())
    if consultas == 0:
        break

    x_div, y_div = map(int, input().split())

    for i in range(consultas):
        x, y = map(int, input().split()) 

        if x == x_div or y == y_div:
            print('divisa')

        elif (x > x_div) and (y > y_div):
            print('NE')
        elif (x > x_div) and (y < y_div):
            print('SE')
        elif (x < x_div) and (y < y_div):
            print('SO')
        else:
            print('NO')
