
quantidade = int(input())
bolas = input().split()

for i in range(1, quantidade):
    temp = []

    for j in range(quantidade - i):
        if bolas[j] == '1' and bolas[j + 1] == '1' or \
            bolas[j] == '-1' and bolas[j + 1] == '-1':
            temp.append('1')
        
        elif bolas[j] == '1' and bolas[j + 1] == '-1' or \
            bolas[j] == '-1' and bolas[j + 1] == '1':
            temp.append('-1')

    bolas = temp.copy()
    
if bolas[0] == '-1':
    print('branca')
else:
    print('preta')
