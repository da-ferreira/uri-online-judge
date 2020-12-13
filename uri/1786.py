
while True:
    try:
        cpf = list(input())
        b1 = b2 = 0

        for i in range(1, 10):
            b1 += int(cpf[i-1]) * i
        
        b1 %= 11 
        if b1 == 10:
            b1 = 0
        
        j = 0
        for i in range(9, 0, -1):
            b2 += int(cpf[j]) * i
            j += 1

        b2 %= 11
        if b2 == 10:
            b2 = 0

        print(f'{cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{b1}{b2}')    
    except EOFError:
        break
