
resp = []

while True:
    n = int(input())
    if n == 0:
        break
    
    temp = n
    n = [x for x in range(1, temp + 1)]

    passes = 1
    i = 0

    continuar = True

    if temp == 13:
        print(1)
    else:
        while continuar:
            if len(n) == 1:
                if n[0] == 13:
                    continuar = False
                else:
                    passes += 1
                    n = [x for x in range(1, temp + 1)]
            else:
                n.pop(i)
                i = (passes + i) % len(n)
        print(passes + 1)   
