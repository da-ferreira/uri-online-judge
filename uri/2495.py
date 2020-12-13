
while True:
    try:
        quantidade = int(input())
        conjunto = {x for x in range(1, quantidade + 1)}

        i = 0
        while True:
            temp = input().split()
            i += len(temp)
            
            for j in range(len(temp)):
                conjunto.remove(int(temp[j]))
            
            if i == quantidade - 1:
                break
            
        print(list(conjunto)[0])
    except EOFError:
        break
