
while True:
    try:
        n, datas = map(int, input().split())

        todas_datas = []
        for i in range(datas):
            entrada = input().partition(' ')
            pessoas = entrada[2].split()
            
            if pessoas.count('1') == n:
                todas_datas.append(entrada[0])
        
        if len(todas_datas) > 0:
            print(todas_datas[0])
        else:
            print('Pizza antes de FdI')
    except EOFError:
        break

