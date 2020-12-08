
casos = int(input())

for i in range(casos):
    sudoku = []
    continuar = True

    for j in range(9):
        sudoku.append(input().split())
    

    for j in range(9):
        temp = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        for k in range(9):
            if sudoku[j][k] in temp:
                temp.remove(sudoku[j][k])
            else:
                continuar = False
            
    
    if continuar:
        for j in range(9):
            temp = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

            for k in range(9):
                if sudoku[k][j] in temp:
                    temp.remove(sudoku[k][j])
                else:
                    continuar = False

    apagar_listas_vazias = 0
    if continuar:
        for j in range(9):

            if apagar_listas_vazias == 3:
                del sudoku[0:3]
                apagar_listas_vazias = 0

            regiao_3x3 = [sudoku[0][0:3], sudoku[1][0:3], sudoku[2][0:3]]
            del sudoku[0][0:3], sudoku[1][0:3], sudoku[2][0:3]

            temp = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

            for k in range(3):
                for l in range(3):
                    if regiao_3x3[k][l] in temp:
                        temp.remove(regiao_3x3[k][l])
                    else:
                        continuar = False
            
            apagar_listas_vazias += 1


    print(f'Instancia {i + 1}')
    if continuar:
        print('SIM')
    else:
        print('NAO')
    print()
