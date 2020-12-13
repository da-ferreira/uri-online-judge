
l, a, p, r = map(int, input().split())

diagonal_caixa = (l ** 2) + (a ** 2) + (p ** 2)

if diagonal_caixa > 4 * r * r:
    print('N') 
else:
    print('S')
