
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break

    if a == 0 and b == 1:
        print(1)
    else:     
        termo1 = 0
        termo2 = 1
        fibonacci = termo1 + termo2

        if a == 0 or a == 1:
            quantidade = 1
        else:
            quantidade = 0

        while fibonacci <= b:
            termo1 = termo2
            termo2 = fibonacci
            fibonacci = termo1 + termo2
            
            if fibonacci >= a and fibonacci <= b:
                quantidade += 1

        print(quantidade)
