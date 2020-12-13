def mmc(a, b, c):
    from math import gcd
    
    result = a * b // gcd(a, b)
    result = result * c // gcd(result, c)

    return result


while True:
    try:
        m = int(input())
        l1, l2, l3 = map(int, input().split())

        resultado = mmc(l1, l2, l3)
        print(resultado - m)
    except EOFError:
        break

