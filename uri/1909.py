
def mmc(bolas, tempo):
    from math import gcd
    
    lcm = bolas[0]

    for i in range(1, len(bolas)):
        lcm = lcm * bolas[i] // gcd(lcm, bolas[i])

    i = 2
    temp = lcm
    bolas = set(bolas)

    while i <= tempo + 1:
        if i not in bolas:
            temp = temp * i // gcd(temp, i)

            if temp == tempo:
                return i
            
            temp = lcm
            
        i += 1
     
    return 'impossivel'


while True:
    n, t = map(int, input().split())
    if n == 0 and t == 0:
        break

    balls = list(map(int, input().split()))
    resultado = mmc(balls, t)

    print(resultado)
