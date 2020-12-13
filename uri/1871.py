
while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    
    soma = str(m + n)
    if '0' in soma:
        soma = soma.replace('0', '')
        print(soma)
    else:
        print(soma)
