
while True:
    quantidade = int(input())
    if quantidade == 0:
        break
    
    for i in range(quantidade):
        civilizacao, chegada, tempo = input().split()
        
        if i == 0:
            nome = civilizacao
            result_temp = int(chegada) - int(tempo)
        else:
            if (int(chegada) - int(tempo)) < result_temp:
                nome = civilizacao
                result_temp = int(chegada) - int(tempo)
    print(nome)
