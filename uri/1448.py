


#Feito em python 2.7 porque tem algum problema com esse
#exercicio no URI que o 3 em diante não funciona (RuntimeError)

casos = int(raw_input())

for i in range(casos):
    frase_original = raw_input()
    time1 = raw_input()
    time2 = raw_input()

    estatistica_time1 = [0, 0]
    estatistica_time2 = [0, 0]

    errou_primeiro = True
    menor = min(len(frase_original), len(time1), len(time2))


    for j in range(menor):
        if frase_original[j] == time1[j]:
            estatistica_time1[0] += 1

        if frase_original[j] == time2[j]:
            estatistica_time2[0] += 1

        if frase_original[j] != time1[j] and frase_original[j] == time2[j] and errou_primeiro:
            estatistica_time1[1] = 1
            errou_primeiro = False
        
        elif frase_original[j] == time1[j] and frase_original[j] != time2[j] and errou_primeiro:
            estatistica_time2[1] = 1
            errou_primeiro = False
            
            
    print 'Instancia', i + 1
    
    if estatistica_time1[0] > estatistica_time2[0]:
        print 'time 1'
    elif estatistica_time1[0] < estatistica_time2[0]:
        print 'time 2'
    else:
        if estatistica_time1[1] < estatistica_time2[1]:
            print 'time 1'
        elif estatistica_time1[1] > estatistica_time2[1]:
            print 'time 2'
        else:
            print 'empate' 
    
    print
