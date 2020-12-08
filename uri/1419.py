
while True:
    rodadas = int(input())
    if rodadas == 0:
        break

    mark_pontos = leti_pontos = 0

    mark = list(map(int, input().split()))
    leti = list(map(int, input().split()))

    pontos_extras = True

    temp_mark, temp_leti = [], []

    for i in range(rodadas):
        mark_pontos += mark[i]
        leti_pontos += leti[i]

        if pontos_extras:
            if i == 0:
                temp_mark.append(mark[i])
                temp_leti.append(leti[i])
            else:
                if mark[i] == temp_mark[-1]:
                    temp_mark.append(mark[i])
                else:
                    temp_mark = [mark[i]]

                if leti[i] == temp_leti[-1]:
                    temp_leti.append(leti[i])
                else:
                    temp_leti = [leti[i]]

            if len(temp_mark) == 3 or len(temp_leti) == 3:
                if len(temp_mark) != len(temp_leti):
                    if len(temp_mark) == 3:
                        mark_pontos += 30
                    else:
                        leti_pontos += 30
                
                pontos_extras = False

    if mark_pontos > leti_pontos:
        print('M')
    elif mark_pontos < leti_pontos:
        print('L')
    else:
        print('T')
