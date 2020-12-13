
def mdc(a, b):
    resto = None

    while resto != 0:
        resto = a % b
        a = b
        b = resto
    
    return a


while True:
    try:
        x, y = map(int, input().split())
        temp = mdc(x, y)
        result = ((x // temp) * 2) + ((y // temp) * 2)
        
        print(result)
    except EOFError:
        break
