
while True:
    n = int(input())
    if n == 0:
        break
    
    alternativas = ['A', 'B', 'C', 'D', 'E']
    
    for i in range(n):
        respostas = list(map(int, input().split()))
        menor_que_127 = 0

        for cor in respostas:
            if cor <= 127:
                menor_que_127 += 1
   
        if (max(respostas) <= 127) or (respostas.count(min(respostas)) > 1) or menor_que_127 > 1 or menor_que_127 == 0:
            print('*')
        else:
            print(alternativas[respostas.index(min(respostas))])
