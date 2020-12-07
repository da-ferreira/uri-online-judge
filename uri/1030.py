
casos = int(input())

for i in range(1, casos + 1):
    n, salto = map(int, input().split())

    n = [x for x in range(1, n + 1)]

    if salto > len(n):
        passes = salto
        j = 0

        while passes > 0:
            if j == len(n):
                j = 0
            
            j += 1
            passes -= 1
        
        j -= 1
    else:
        j = salto - 1   

    salto -= 1
    
    while len(n) != 1:
        n.pop(j)
        j = (j + salto) % len(n)  # modo de saltar as pessoas sem precisar de "força bruta".   
    
    print(f'Case {i}: {n[0]}')
