
def eh_possivel(a, b, c, d):
    if (a + b) == (c + d):
        return True

    elif (a + c) == (b + d):
        return True

    elif (a + d) == (b + c):
        return True

    elif a == (b + c + d):
        return True

    elif b == (a + c + d):
        return True

    elif c == (a + b + d):
        return True

    elif d == (a + b + c):
        return True

    return False

valor_a, resto_a = input().split('.')
valor_a = int(valor_a) * 10 + int(resto_a)

valor_b, resto_b = input().split('.')
valor_b = int(valor_b) * 10 + int(resto_b)

valor_c, resto_c = input().split('.')
valor_c = int(valor_c) * 10 + int(resto_c)

valor_d, resto_d = input().split('.')
valor_d = int(valor_d) * 10 + int(resto_d)

if eh_possivel(valor_a, valor_b, valor_c, valor_d):
    print('YES')
else:
    print('NO')
