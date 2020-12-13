
while True:
    comida = int(input())
    if comida == 0:
        break

    picapau = fink = 0

    i = 1
    while True:
        picapau += 1
        fink += i
        
        comida -= 1  # tirando a que o picapau pegou

        if comida - i < 0:
            picapau -= abs(comida - i)
            comida = 0
        else:   
            comida -= i

        if comida == 0:
            break

        i += 1
    
    print(fink, picapau)
