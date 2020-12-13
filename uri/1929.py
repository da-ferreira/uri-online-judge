
def criar_triangulo(r1, r2, r3):
    if ((r2 - r3) < r1 < (r2 + r3)) and \
        ((r1 - r3) < r2 < (r1 + r3)) and \
        ((r1 - r2) < r3 < (r1 + r2)):
        return True
    else:
        return False


A, B, C, D = map(int, input().split())

if criar_triangulo(A, B, C) or criar_triangulo(A, B, D) or criar_triangulo(B, C, D) or criar_triangulo(C, D, A):
    print('S')   
else:
    print('N')
