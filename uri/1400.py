
while True:
    n, m, k = map(int, input().split())
    if n == 0:
        break

    pessoas = [0] * (n + 1)
    k_esima = 0
    i = 1
    j = 1
    indo = True

    if m > n:
        print(0)
    else:
        while k_esima < k:
            if indo:
                pessoas[i] = j

                if (i == m and pessoas[i] % 7 == 0) or (i == m and '7' in str(pessoas[i])):
                    k_esima += 1
                
                if i == n:

                    i = n - 1
                    indo = False
                else:
                    i += 1

            else:
                pessoas[i] = j

                if (i == m and pessoas[i] % 7 == 0) or (i == m and '7' in str(pessoas[i])):
                    k_esima += 1
                
                if i == 1:

                    i = 2
                    indo = True
                else:
                    i -= 1
            
            j += 1
        
        print(pessoas[m])
