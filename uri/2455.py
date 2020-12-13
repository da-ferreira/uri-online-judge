
p1, c1, p2, c2 = map(int, input().split())

lado_esquerdo = p1 * c1
lado_direito = p2 * c2

if lado_esquerdo == lado_direito:
    print('0')
elif lado_esquerdo > lado_direito:
    print('-1')
else:
    print('1')
    