
while True:
    try:
        enesimo = int(input())

        if enesimo == 1:
            print(3)
        else:
            termo = '3'

            for i in range(enesimo - 1):
                temp = [termo[0], 1]
                
                if len(termo) == 1:
                    temp2 = str(temp[1]) + temp[0] 
                else:
                    temp2 = ''

                for j in range(len(termo) - 1):
                    if temp[0] == termo[j + 1]:
                        temp[1] += 1
                    else:
                        temp2 += str(temp[1]) + temp[0]
                        temp = [termo[j + 1], 1]

                        if j + 1 == len(termo) - 1:
                            temp2 += str(temp[1]) + temp[0]

                termo = temp2

            print(termo)
    except EOFError:
        break
